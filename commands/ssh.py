#!/usr/bin/env python3
"""
SSH key generation commands.
Handles the execution of ssh-keygen and related operations.
"""

import subprocess
import os
from pathlib import Path


def generate_ssh_key(ssh_comment, privkey_dir, pubkey_dir, key_name="id_ed25519"):
    """
    Generate an SSH key pair using ssh-keygen command with Ed25519 algorithm.
    
    Args:
        ssh_comment (str): Comment to include in the SSH key
        privkey_dir (str): Directory where private key will be saved
        pubkey_dir (str): Directory where public key will be saved
        key_name (str): Name of the key file (default: "id_ed25519")
    
    Returns:
        tuple: (success: bool, message: str, private_key_path: str, public_key_path: str)
    """
    # Validate inputs
    if not ssh_comment:
        return False, "SSH comment is required", None, None
    
    if not privkey_dir or not pubkey_dir:
        return False, "Both private and public key directories are required", None, None
    
    # Create directories if they don't exist
    try:
        Path(privkey_dir).mkdir(parents=True, exist_ok=True)
        Path(pubkey_dir).mkdir(parents=True, exist_ok=True)
    except Exception as e:
        return False, f"Failed to create directories: {str(e)}", None, None
    
    # Construct file paths
    private_key_path = os.path.join(privkey_dir, key_name)
    public_key_path = os.path.join(pubkey_dir, f"{key_name}.pub")
    
    # Check if keys already exist
    if os.path.exists(private_key_path):
        return False, f"Private key already exists: {private_key_path}", None, None
    
    # Build ssh-keygen command for Ed25519
    # -t ed25519: Ed25519 key type (modern, secure algorithm)
    # -f: output file path
    # -C: comment
    # -N "": no passphrase (empty string)
    cmd = [
        'ssh-keygen',
        '-t', 'ed25519',
        '-f', private_key_path,
        '-C', ssh_comment,
        '-N', ''  # No passphrase
    ]
    
    try:
        # Execute ssh-keygen command
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Move public key to specified directory if needed
        # (ssh-keygen creates .pub file next to private key)
        generated_pubkey = f"{private_key_path}.pub"
        if os.path.exists(generated_pubkey) and generated_pubkey != public_key_path:
            os.rename(generated_pubkey, public_key_path)
        
        return True, "SSH key generated successfully", private_key_path, public_key_path
        
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if e.stderr else e.stdout
        return False, f"Failed to generate SSH key: {error_msg}", None, None
    except FileNotFoundError:
        return False, "ssh-keygen command not found. Please ensure OpenSSH is installed.", None, None
    except Exception as e:
        return False, f"Unexpected error: {str(e)}", None, None

