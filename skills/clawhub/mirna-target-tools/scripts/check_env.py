#!/usr/bin/env python3
"""
Check if required bioinformatics tools are installed.
"""

import shutil
import sys
import subprocess

required_tools = {
    'targetscan': 'TargetScan',
    'miranda': 'miRanda',
    'cytoscape': 'Cytoscape'
}

required_packages = ['pandas', 'numpy']
optional_packages = {
    'mygene': 'gene annotation (annotate_targets.py)',
    'matplotlib': 'publication plots (plot_enrichment.py, conservation_analysis.py)',
}


def check_tool(tool_name):
    return shutil.which(tool_name) is not None


def main():
    print("Checking bioinformatics environment...\n")

    all_found = True
    missing = []

    for tool, display in required_tools.items():
        if check_tool(tool):
            print(f"✅ {display} found")
        else:
            print(f"❌ {display} not found in PATH")
            missing.append(display)
            all_found = False

    # Required Python packages
    print("\nChecking required Python packages...")
    for pkg in required_packages:
        try:
            __import__(pkg)
            print(f"✅ {pkg} installed")
        except ImportError:
            print(f"❌ {pkg} not installed")
            missing.append(f"Python {pkg}")
            all_found = False

    # Optional Python packages (for annotation / plotting)
    print("\nChecking optional Python packages...")
    for pkg, purpose in optional_packages.items():
        try:
            __import__(pkg)
            print(f"✅ {pkg} installed (for {purpose})")
        except ImportError:
            print(f"⚠️  {pkg} not installed (optional, for {purpose})")

    print(f"\n{'All required dependencies installed!' if all_found else 'Missing required dependencies detected.'}")

    if not all_found:
        print("\nTo install missing dependencies, run:")
        print("  bash scripts/install_dependencies.sh")
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
