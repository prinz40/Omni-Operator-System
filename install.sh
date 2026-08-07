#!/bin/bash
echo "Installing OMNI-OPERATOR v2.0..."
pkg update && pkg install python git -y
pip install -r requirements.txt
echo "Installation complete! Run: python orchestrator_dashboard.py"
