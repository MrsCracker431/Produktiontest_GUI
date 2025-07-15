<<<<<<< HEAD
import customtkinter as ctk
from tkinter import font
import threading
import time
from test_runner.test_executor import TestExecutor
from gui.colors import Colors

class TestWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Production Test")
        self.geometry("800x600")
        self.minsize(600, 400)
        
        # State management
        self.current_state = "idle"  # idle, testing, pass, fail
        self.test_executor = TestExecutor()
        
        # Configure grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.create_widgets()
        self.update_ui_state("idle")
        
    def create_widgets(self):
        # Status Label
        self.status_label = ctk.CTkLabel(
            self,
            text="Ready to Test",
            font=ctk.CTkFont(size=48, weight="bold")
        )
        self.status_label.grid(row=0, column=0, pady=20)
        
        # Main Button
        self.main_button = ctk.CTkButton(
            self,
            text="START TEST",
            command=self.toggle_test,
            width=300,
            height=100,
            font=ctk.CTkFont(size=32, weight="bold"),
            corner_radius=20
        )
        self.main_button.grid(row=1, column=0)
        
        # Results Frame (hidden initially)
        self.results_frame = ctk.CTkFrame(self)
        self.results_label = ctk.CTkLabel(
            self.results_frame,
            text="",
            font=ctk.CTkFont(size=18),
            justify="left"
        )
        self.results_label.pack(padx=20, pady=20)
        
    def toggle_test(self):
        if self.current_state == "idle":
            self.start_test()
        elif self.current_state == "testing":
            self.stop_test()
        elif self.current_state in ["pass", "fail"]:
            self.update_ui_state("idle")
            self.after(100, self.start_test)
    def reset_and_start(self):
        self.update_ui_state("idle")
        self.after(100, self.start_test)
            
    def start_test(self):
        self.update_ui_state("testing")
        # Run tests in separate thread
        self.test_thread = threading.Thread(target=self.run_tests)
        self.test_thread.daemon = True
        self.test_thread.start()
        
    def stop_test(self):
        self.test_executor.stop_tests()
        self.update_ui_state("idle")
        
    def run_tests(self):
        results = self.test_executor.run_all_tests()
        
        if results["all_passed"]:
            self.after(0, lambda: self.update_ui_state("pass"))
        else:
            self.after(0, lambda: self.show_failures(results["failures"]))
            self.after(0, lambda: self.update_ui_state("fail"))
            
    def show_failures(self, failures):
        failure_text = "Failed Tests:\n\n"
        for failure in failures:
            failure_text += f"❌ {failure['name']}: {failure['reason']}\n"
        self.results_label.configure(text=failure_text)
        
    def update_ui_state(self, state):
        self.current_state = state
        
        if state == "idle":
            self.configure(fg_color=Colors.IDLE_BG)
            self.status_label.configure(text="Ready to Test", text_color=Colors.IDLE_TEXT)
            self.main_button.configure(text="START TEST", fg_color=Colors.BUTTON_START, state="normal")
            self.results_frame.grid_forget()
            
        elif state == "testing":
            self.configure(fg_color=Colors.TESTING_BG)
            self.status_label.configure(text="Testing in Progress...", text_color="white")
            self.main_button.configure(text="STOP TEST", fg_color=Colors.BUTTON_STOP, state="normal")
            self.results_frame.grid_forget()
            
        elif state == "pass":
            self.configure(fg_color=Colors.PASS_BG)
            self.status_label.configure(text="✓ TEST PASSED", text_color="white")
            self.main_button.configure(text="START TEST", fg_color=Colors.BUTTON_START, state="normal")
            self.results_frame.grid_forget()
            #Reset state to idle

            self.after(3000, lambda: self.update_ui_state("idle") if self.current_state == "pass" else None)
            
        elif state == "fail":
            self.configure(fg_color=Colors.FAIL_BG)
            self.status_label.configure(text="✗ TEST FAILED", text_color="white")
            self.main_button.configure(text="START TEST", fg_color=Colors.BUTTON_START, state="normal")
            self.results_frame.grid(row=2, column=0, padx=40, pady=20, sticky="ew")
            self.results_frame.configure(fg_color=Colors.FAIL_RESULTS_BG)
            #Update button to command to restet state
=======
import customtkinter as ctk
from tkinter import font
import threading
import time
from test_runner.test_executor import TestExecutor
from gui.colors import Colors

class TestWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Production Test")
        self.geometry("800x600")
        self.minsize(600, 400)
        
        # State management
        self.current_state = "idle"  # idle, testing, pass, fail
        self.test_executor = TestExecutor()
        
        # Configure grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.create_widgets()
        self.update_ui_state("idle")
        
    def create_widgets(self):
        # Status Label
        self.status_label = ctk.CTkLabel(
            self,
            text="Ready to Test",
            font=ctk.CTkFont(size=48, weight="bold")
        )
        self.status_label.grid(row=0, column=0, pady=20)
        
        # Main Button
        self.main_button = ctk.CTkButton(
            self,
            text="START TEST",
            command=self.toggle_test,
            width=300,
            height=100,
            font=ctk.CTkFont(size=32, weight="bold"),
            corner_radius=20
        )
        self.main_button.grid(row=1, column=0)
        
        # Results Frame (hidden initially)
        self.results_frame = ctk.CTkFrame(self)
        self.results_label = ctk.CTkLabel(
            self.results_frame,
            text="",
            font=ctk.CTkFont(size=18),
            justify="left"
        )
        self.results_label.pack(padx=20, pady=20)
        
    def toggle_test(self):
        if self.current_state == "idle":
            self.start_test()
        elif self.current_state == "testing":
            self.stop_test()
        elif self.current_state in ["pass", "fail"]:
            self.update_ui_state("idle")
            self.after(100, self.start_test)
    def reset_and_start(self):
        self.update_ui_state("idle")
        self.after(100, self.start_test)
            
    def start_test(self):
        self.update_ui_state("testing")
        # Run tests in separate thread
        self.test_thread = threading.Thread(target=self.run_tests)
        self.test_thread.daemon = True
        self.test_thread.start()
        
    def stop_test(self):
        self.test_executor.stop_tests()
        self.update_ui_state("idle")
        
    def run_tests(self):
        results = self.test_executor.run_all_tests()
        
        if results["all_passed"]:
            self.after(0, lambda: self.update_ui_state("pass"))
        else:
            self.after(0, lambda: self.show_failures(results["failures"]))
            self.after(0, lambda: self.update_ui_state("fail"))
            
    def show_failures(self, failures):
        failure_text = "Failed Tests:\n\n"
        for failure in failures:
            failure_text += f"❌ {failure['name']}: {failure['reason']}\n"
        self.results_label.configure(text=failure_text)
        
    def update_ui_state(self, state):
        self.current_state = state
        
        if state == "idle":
            self.configure(fg_color=Colors.IDLE_BG)
            self.status_label.configure(text="Ready to Test", text_color=Colors.IDLE_TEXT)
            self.main_button.configure(text="START TEST", fg_color=Colors.BUTTON_START, state="normal")
            self.results_frame.grid_forget()
            
        elif state == "testing":
            self.configure(fg_color=Colors.TESTING_BG)
            self.status_label.configure(text="Testing in Progress...", text_color="white")
            self.main_button.configure(text="STOP TEST", fg_color=Colors.BUTTON_STOP, state="normal")
            self.results_frame.grid_forget()
            
        elif state == "pass":
            self.configure(fg_color=Colors.PASS_BG)
            self.status_label.configure(text="✓ TEST PASSED", text_color="white")
            self.main_button.configure(text="START TEST", fg_color=Colors.BUTTON_START, state="normal")
            self.results_frame.grid_forget()
            #Reset state to idle

            self.after(3000, lambda: self.update_ui_state("idle") if self.current_state == "pass" else None)
            
        elif state == "fail":
            self.configure(fg_color=Colors.FAIL_BG)
            self.status_label.configure(text="✗ TEST FAILED", text_color="white")
            self.main_button.configure(text="START TEST", fg_color=Colors.BUTTON_START, state="normal")
            self.results_frame.grid(row=2, column=0, padx=40, pady=20, sticky="ew")
            self.results_frame.configure(fg_color=Colors.FAIL_RESULTS_BG)
            #Update button to command to restet state
>>>>>>> 7219fbe912656346efc7d1ff426f83e2809bddf7
            self.main_button.configure(command=self.reset_and_start)