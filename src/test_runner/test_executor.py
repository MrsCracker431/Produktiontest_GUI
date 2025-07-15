<<<<<<< HEAD
import subprocess
import time
import os
import sys

class TestExecutor:
    def __init__(self):
        self.process = None
        self.stop_flag = False
        
    def run_all_tests(self):
        results = {
            "all_passed": False,
            "failures": []
        }
        
        try:
            # Run pytest with simple output parsing
            cmd = [sys.executable, '-m', 'pytest', ]
            
            self.process = subprocess.Popen(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            # Parse output in real-time
            for line in self.process.stdout:
                if self.stop_flag:
                    print(line.split())
                    self.process.terminate()
                    break
                    
                # Look for test failures
                if "FAILED" in line:
                    # Extract failure info from pytest output
                    test_name = line.split("::")[1].split()[0] if "::" in line else "Unknown test"
                    results["failures"].append({
                        "name": test_name,
                        "reason": "Test assertion failed"
                    })
            
            self.process.wait()
            results["all_passed"] = (self.process.returncode == 0)
            
        except Exception as e:
            results["failures"].append({
                "name": "Test Execution Error",
                "reason": str(e)[:50]
            })
            
        return results
        
    def stop_tests(self):
        self.stop_flag = True
        if self.process:
            self.process.terminate()

#heh
=======
import subprocess
import time
import os
import sys

class TestExecutor:
    def __init__(self):
        self.process = None
        self.stop_flag = False
        
    def run_all_tests(self):
        results = {
            "all_passed": False,
            "failures": []
        }
        
        try:
            # Run pytest with simple output parsing
            cmd = [sys.executable, '-m', 'pytest', ]
            
            self.process = subprocess.Popen(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            # Parse output in real-time
            for line in self.process.stdout:
                if self.stop_flag:
                    print(line.split())
                    self.process.terminate()
                    break
                    
                # Look for test failures
                if "FAILED" in line:
                    # Extract failure info from pytest output
                    test_name = line.split("::")[1].split()[0] if "::" in line else "Unknown test"
                    results["failures"].append({
                        "name": test_name,
                        "reason": "Test assertion failed"
                    })
            
            self.process.wait()
            results["all_passed"] = (self.process.returncode == 0)
            
        except Exception as e:
            results["failures"].append({
                "name": "Test Execution Error",
                "reason": str(e)[:50]
            })
            
        return results
        
    def stop_tests(self):
        self.stop_flag = True
        if self.process:
            self.process.terminate()
>>>>>>> 7219fbe912656346efc7d1ff426f83e2809bddf7
