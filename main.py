import time
import random
import os

class RubiksCubeApp:
    def __init__(self):
        self.solve_times = []
        self.scramble_history = []
        self.load_data()
    
    def main_menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
            print("===== RUBIK'S CUBE TIMER =====")
            print("1. Start Timer")
            print("2. View Solve History")
            print("3. Generate Scramble")
            print("4. Cube Visualization")
            print("5. Exit")
        
            choice = input("Enter your choice (1-5): ")
        
            if choice == '1':
                self.start_timer()
            elif choice == '2':
                self.view_history()
            elif choice == '3':
                self.generate_scramble(display=True)
                input("Press Enter to continue...")
            elif choice == '4':
                self.display_cube()
            elif choice == '5':
                self.save_data()
                print("Your solve history has been saved!")
                print("Thank you for using the Rubik's Cube Timer!")
                break
        else:
            input("Invalid choice. Press Enter to continue...")
    def start_timer(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    # Generate and display a scramble
        scramble = self.generate_scramble(display=True)
    
        input("Press Enter when you're ready to start solving...")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Timer running... Press Enter when done!")
    
        start_time = time.time()
        input()  # Wait for user to press Enter
        end_time = time.time()
    
        solve_time = end_time - start_time
        self.solve_times.append(solve_time)
        self.scramble_history.append(scramble)
    
        print(f"Solve completed in: {solve_time:.2f} seconds")
        input("Press Enter to continue...")
    
    def view_history(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===== SOLVE HISTORY =====")
    
        if not self.solve_times:
            print("No solve history available.")
        else:
            print(f"Total solves: {len(self.solve_times)}")
        
            if len(self.solve_times) >= 3:
                avg_3 = sum(self.solve_times[-3:]) / 3
                print(f"Average of 3: {avg_3:.2f} seconds")
        
            if len(self.solve_times) >= 5:
                avg_5 = sum(self.solve_times[-5:]) / 5
                print(f"Average of 5: {avg_5:.2f} seconds")
        
            if len(self.solve_times) >= 12:
                avg_12 = sum(self.solve_times[-12:]) / 12
                print(f"Average of 12: {avg_12:.2f} seconds")
        
        # Find best time
                best_time = min(self.solve_times)
                best_index = self.solve_times.index(best_time)
                print(f"\nBest time: {best_time:.2f} seconds")
                print(f"Scramble: {self.scramble_history[best_index]}")
        
        # Show recent solves
                print("\nRecent solves:")
                start_idx = max(0, len(self.solve_times) - 5)
                for i in range(start_idx, len(self.solve_times)):
                    print(f"{i+1}. {self.solve_times[i]:.2f} seconds - {self.scramble_history[i]}")
    
    input("\nPress Enter to return to the main menu...")
    
    def generate_scramble(self):
        def generate_scramble(self, display=False):
            moves = ["R", "L", "U", "D", "F", "B"]
            modifiers = ["", "'", "2"]
    
        # Generate a random scramble of 20 moves
        scramble = []
        prev_move = None
    
        for _ in range(20):
            move = random.choice(moves)
            # Avoid repeating the same face
            while move == prev_move:
                move = random.choice(moves)
        
            modifier = random.choice(modifiers)
            scramble.append(move + modifier)
            prev_move = move
    
        scramble_str = " ".join(scramble)
    
        if display:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("===== SCRAMBLE =====")
            print(scramble_str)
            print("===================")
    
        return scramble_str

if __name__ == "__main__":
    app = RubiksCubeApp()
    app.main_menu()

    def save_data(self):
    with open("cube_history.txt", "w") as file:
        for i in range(len(self.solve_times)):
            file.write(f"{self.solve_times[i]},{self.scramble_history[i]}\n")
    
def load_data(self):
    try:
        with open("cube_history.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.strip():  # Check if line is not empty
                    parts = line.strip().split(",", 1)
                    if len(parts) == 2:
                        time_val, scramble = parts
                        self.solve_times.append(float(time_val))
                        self.scramble_history.append(scramble)
    except FileNotFoundError:
        # No existing data file
        pass

def display_cube(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===== CUBE VISUALIZATION =====")
    
    # Simple ASCII representation of a solved cube
    # Using letters W(white), Y(yellow), R(red), O(orange), G(green), B(blue)
    
    # Top face (white)
    print("       W W W")
    print("       W W W")
    print("       W W W")
    
    # Middle layer (G-R-B-O)
    print("G G G  R R R  B B B  O O O")
    print("G G G  R R R  B B B  O O O")
    print("G G G  R R R  B B B  O O O")
    
    # Bottom face (yellow)
    print("       Y Y Y")
    print("       Y Y Y")
    print("       Y Y Y")
    
    input("\nThis is a solved cube. Press Enter to return to the main menu...")