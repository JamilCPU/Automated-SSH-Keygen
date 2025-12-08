#!/usr/bin/env python3
"""
SSH Key Generator GUI Application
GUI for automating SSH key creation with input fields for comment and directories.
"""

import tkinter as tk
from tkinter import ttk, filedialog


class SSHKeyGeneratorApp:
    """Main application window for SSH key generation."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("SSH Key Generator")
        self.root.geometry("600x300")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for resizing
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # SSH Comment field label
        ttk.Label(main_frame, text="SSH Comment:").grid(
            row=0, column=0, sticky=tk.W, pady=10
        )
        
        # SSH Comment field
        self.ssh_comment_var = tk.StringVar()
        self.ssh_comment_entry = ttk.Entry(main_frame, textvariable=self.ssh_comment_var, width=40)
        self.ssh_comment_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=10, padx=(10, 0))
        
        # PrivKey Directory label
        ttk.Label(main_frame, text="PrivKey Directory:").grid(
            row=1, column=0, sticky=tk.W, pady=10
        )
        
        # PrivKey Directory field and browse button
        privkey_frame = ttk.Frame(main_frame)
        privkey_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=10, padx=(10, 0))
        privkey_frame.columnconfigure(0, weight=1)
        
        self.privkey_dir_var = tk.StringVar()
        self.privkey_entry = ttk.Entry(privkey_frame, textvariable=self.privkey_dir_var, width=35)
        self.privkey_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        ttk.Button(privkey_frame, text="Browse", command=self.browse_privkey_dir).grid(
            row=0, column=1, padx=(5, 0)
        )
        
        # PubKey Directory label
        ttk.Label(main_frame, text="PubKey Directory:").grid(
            row=2, column=0, sticky=tk.W, pady=10
        )
        
        # PubKey Directory field and browse button
        pubkey_frame = ttk.Frame(main_frame)
        pubkey_frame.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=10, padx=(10, 0))
        pubkey_frame.columnconfigure(0, weight=1)
        
        self.pubkey_dir_var = tk.StringVar()
        self.pubkey_entry = ttk.Entry(pubkey_frame, textvariable=self.pubkey_dir_var, width=35)
        self.pubkey_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        ttk.Button(pubkey_frame, text="Browse", command=self.browse_pubkey_dir).grid(
            row=0, column=1, padx=(5, 0)
        )
        
        # Generate Key button
        generate_button = ttk.Button(
            main_frame, 
            text="Generate Key", 
            command=self.generate_key
        )
        generate_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Set focus to SSH Comment field
        self.ssh_comment_entry.focus()
    
    def browse_privkey_dir(self):
        """Open directory browser for private key directory."""
        directory = filedialog.askdirectory(title="Select Private Key Directory")
        if directory:
            self.privkey_dir_var.set(directory)
    
    def browse_pubkey_dir(self):
        """Open directory browser for public key directory."""
        directory = filedialog.askdirectory(title="Select Public Key Directory")
        if directory:
            self.pubkey_dir_var.set(directory)
    
    def get_field_values(self):
        """
        Retrieve all input field values.
        
        Returns:
            dict: Dictionary containing all field values:
                - ssh_comment: SSH comment string
                - privkey_dir: Private key directory path
                - pubkey_dir: Public key directory path
        """
        return {
            'ssh_comment': self.ssh_comment_var.get(),
            'privkey_dir': self.privkey_dir_var.get(),
            'pubkey_dir': self.pubkey_dir_var.get()
        }
    
    def generate_key(self):
        """
        Generate SSH key based on user input.
        This function will be expanded with key generation logic.
        """
        # Get all field values
        values = self.get_field_values()
        
        # Output the values (for now)
        print("=" * 50)
        print("SSH Key Generation - Field Values:")
        print("=" * 50)
        print(f"SSH Comment: {values['ssh_comment']}")
        print(f"Private Key Directory: {values['privkey_dir']}")
        print(f"Public Key Directory: {values['pubkey_dir']}")
        print("=" * 50)
        
        # TODO: Add key generation logic here


def main():
    """Entry point for the application."""
    root = tk.Tk()
    app = SSHKeyGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

