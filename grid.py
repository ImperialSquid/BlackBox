from random import shuffle


class Grid:
    def __init__(self, rows=1, cols=1, size=None,
                 atoms=[], atom_num=0):
        if size is not None:
            rows = size[0]
            cols = size[1]

        self.dims = [rows, cols]

        self.grid = []
        for row in range(rows):
            self.grid.append([])
            for col in range(cols):
                self.grid[-1].append(".")

        self.add_atoms(atoms)

        self.add_random_atoms(atom_num)

    def add_atoms(self, atoms=[]):
        if isinstance(atoms, list) and len(atoms) > 0:
            for atom in atoms:
                try:
                    self.grid[atom[0]][atom[1]] = "#"
                except ValueError:
                    pass

    def remove_atoms(self, atoms):
        if isinstance(atoms, list) and len(atoms) > 0:
            for atom in atoms:
                try:
                    self.grid[atom[0]][atom[1]] = "."
                except ValueError:
                    pass

    def get_atoms(self):
        atoms = []
        for r, row in enumerate(self.grid):
            for c, space in enumerate(row):
                if space == "#":
                    atoms.append([r,c])

        return atoms
    
    def get_free_spaces(self):
        free_spaces = []
        for r, row in enumerate(self.grid):
            for c, space in enumerate(row):
                if space == ".":
                    free_spaces.append([r, c])

        return free_spaces

    def add_random_atoms(self, num_atoms):
        if isinstance(num_atoms, int) and num_atoms > 0:
            spaces = self.get_free_spaces()
            num_spaces = len(spaces)
            if num_spaces == 0:
                pass
            elif num_spaces < num_atoms:
                num_atoms = num_spaces

            shuffle(spaces)
            new_atoms = spaces[:num_atoms]
            self.add_atoms(new_atoms)
        else:
            pass
            # invalid atom num_atoms

    def print_grid(self):
        print("Dims: {0}x{1}".format(*self.dims))
        print("  "+"".join([str(c) for c in range(self.dims[1])]))
        for r, row in enumerate(self.grid):
            print(str(r)+" ", *row, sep="")
