import sys                        # Yahan pe hum sys module import kar rahe hain, taki command line arguments use kar saken

class Node():                      # Ye ek Node class hai, socho maze ke har point ko ek node ki tarah treat kar rahe hain
    def _init_(self, state, parent, action): # Constructor hai, state yani position, parent yani previous node, action yani move
        self.state = state         # Yahan pe node ki position store ho rahi hai
        self.parent = parent       # Parent node store ho rahi hai
        self.action = action       # Kis action se yahan aaye, wo store ho raha hai

class StackFrontier():             # Ye StackFrontier class hai, LIFO principle follow karti hai, yani jo last aaya wo pehle niklega
    def _init_(self):
        self.frontier = []         # Frontier ek list hai, jisme nodes store karte hain

    def add(self, node):           # Frontier mein naya node add karne ke liye
        self.frontier.append(node)

    def contains_state(self, state): # Check karte hain kya ye state frontier mein already hai
        return any(node.state == state for node in self.frontier)

    def empty(self):               # Frontier empty hai ya nahi, check karte hain
        return len(self.frontier) == 0

    def remove(self):              # Frontier se last node nikalte hain
        if self.empty():
            raise Exception("empty frontier") # Agar empty hai to error throw karte hain
        else:
            node = self.frontier[-1]         # Last node lete hain
            self.frontier = self.frontier[:-1] # Usko list se hata dete hain
            return node

class QueueFrontier(StackFrontier): # Ye QueueFrontier hai, FIFO principle follow karti hai
    def remove(self):
        if self.empty():
            raise Exception("empty frontier") # Agar empty hai to error throw karte hain
        else:
            node = self.frontier[0]           # Sabse pehla node lete hain
            self.frontier = self.frontier[1:] # Usko list se hata dete hain
            return node

class Maze():
    def _init_(self, filename):
        # Yahan pe maze file read kar rahe hain, aur maze ki height aur width set kar rahe hain
        with open(filename) as f:
            contents = f.read()

        # Check karte hain maze mein ek hi start (A) aur ek hi goal (B) ho
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # Maze ki height aur width nikalte hain
        contents = contents.splitlines()
        self.height = len(contents) # Kitni rows hain
        self.width = max(len(line) for line in contents) # Sabse lambi row ki length

        # Walls ka track rakhte hain
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)   # Start point mil gaya
                        row.append(False)     # Yahan wall nahi hai
                    elif contents[i][j] == "B":
                        self.goal = (i, j)   # Goal point mil gaya
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)     # Khali jagah hai
                    else:
                        row.append(True)      # Wall hai
                except IndexError:
                    row.append(False)         # Agar index out ho jaye to khali treat karte hain
            self.walls.append(row)

        self.solution = None                  # Solution abhi tak nahi mila

    def print(self):
        # Maze ko print karte hain, taki hum dekh saken kaisa lag raha hai
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")      # Wall ko block se show karte hain
                elif (i, j) == self.start:
                    print("A", end="")      # Start point show karte hain
                elif (i, j) == self.goal:
                    print("B", end="")      # Goal point show karte hain
                elif solution is not None and (i, j) in solution:
                    print("*", end="")      # Solution path ko star se show karte hain
                else:
                    print(" ", end="")      # Khali jagah
            print()
        print()

    def neighbors(self, state):
        # Kisi bhi state ke neighbors nikalte hain, yani agle possible moves
        row, col = state
        candidates = [
            ("up", (row - 1, col)),    # Upar jana
            ("down", (row + 1, col)),  # Neeche jana
            ("left", (row, col - 1)),  # Left jana
            ("right", (row, col + 1))  # Right jana
        ]
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c))) # Agar wall nahi hai to neighbor add karte hain
        return result

    def solve(self):
        """Maze ka solution nikalte hain, agar exist karta hai."""
        self.num_explored = 0              # Kitni states explore ki hain
        start = Node(state=self.start, parent=None, action=None) # Start node banate hain
        frontier = StackFrontier()         # Frontier banate hain
        frontier.add(start)                # Start node frontier mein daal dete hain
        self.explored = set()              # Explored states ka set

        while True:
            if frontier.empty():           # Agar frontier empty ho gaya to solution nahi mila
                raise Exception("no solution")

            node = frontier.remove()       # Frontier se ek node nikalte hain
            self.num_explored += 1         # Explored count badhate hain

            if node.state == self.goal:    # Agar goal mil gaya
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action) # Har action ko list mein daal rahe hain
                    cells.append(node.state)    # Har cell ko list mein daal rahe hain
                    node = node.parent          # Parent pe chalte hain
                actions.reverse()              # List ko reverse karte hain taki start se goal tak ho
                cells.reverse()
                self.solution = (actions, cells) # Solution mil gaya
                return

            self.explored.add(node.state)      # Current node ko explored mein daal dete hain

            for action, state in self.neighbors(node.state): # Har neighbor ke liye
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action) # Naya node banate hain
                    frontier.add(child)                                 # Frontier mein daal dete hain

    def output_image(self, filename, show_solution=True, show_explored=False):
        # Maze ka image banate hain, taki visually dekh saken
        from PIL import Image, ImageDraw

        cell_size = 50              # Har cell ki size
        cell_border = 2             # Border ki width

        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None

        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    fill = (40, 40, 40)      # Wall ka color
                elif (i, j) == self.start:
                    fill = (255, 0, 0)       # Start ka color
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)      # Goal ka color
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)   # Solution path ka color
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)     # Explored cells ka color
                else:
                    fill = (237, 240, 252)   # Empty cell ka color

                draw.rectangle(
                    [
                        (j * cell_size + cell_border, i * cell_size + cell_border),
                        ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)
                    ],
                    fill=fill
                )
        img.save(filename)           # Image save kar dete hain

if __name__ == "__main__":
    # Yahan se program start hota hai
    if len(sys.argv) != 2:
        sys.exit("Usage: python maze.py maze.txt") # Agar argument sahi nahi diya to error
    m = Maze(sys.argv[1])
    print("Maze:")
    m.print()                   # Maze print karte hain
    print("Solving...")
    m.solve()                   # Maze solve karte hain
    print("States Explored:", m.num_explored) # Kitni states explore hui
    print("Solution:")
    m.print()                   # Solution print karte hain
    m.output_image("maze.png", show_explored=True) # Maze ka image bana ke save karte hain