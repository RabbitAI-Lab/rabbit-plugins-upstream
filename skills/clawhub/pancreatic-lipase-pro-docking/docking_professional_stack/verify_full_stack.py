#!/usr/bin/env python3
"""Categorized verification for the full docking/simulation environment."""
from __future__ import annotations
import importlib.util, shutil, subprocess, sys, json, platform

CATEGORIES = {
    "core_python": ["numpy", "scipy", "pandas", "sklearn", "matplotlib", "yaml", "joblib", "requests"],
    "cheminformatics": ["rdkit", "openbabel", "meeko", "datamol", "selfies", "mols2grid", "spyrmsd"],
    "structure_biology": ["Bio", "gemmi", "pdbfixer", "mdtraj", "MDAnalysis", "freesasa", "propka", "pdb2pqr"],
    "interaction_analysis": ["plip", "prolif", "oddt"],
    "simulation": ["openmm", "openff", "parmed"],
    "data_apis": ["pubchempy", "chembl_webresource_client"],
    "workflow_scaling": ["dask", "distributed", "snakemake", "psutil", "diskcache", "duckdb", "polars"],
    "free_energy_optional": ["openfe", "cinnabar"],
}

COMMANDS = {
    "docking": ["vina", "smina", "obabel", "mk_prepare_ligand.py", "mk_prepare_receptor.py"],
    "pocket_detection": ["fpocket"],
    "simulation": ["gmx", "antechamber", "tleap", "MMPBSA.py"],
    "workflow": ["parallel", "snakemake"],
}

ALIASES = {
    "sklearn": "sklearn",
    "Bio": "Bio",
    "yaml": "yaml",
    "openff": "openff",
}

def has_module(name: str) -> bool:
    return importlib.util.find_spec(ALIASES.get(name, name)) is not None

def cmd_version(cmd: str):
    path = shutil.which(cmd)
    if not path:
        return None, None
    for args in ([cmd, "--version"], [cmd, "-h"]):
        try:
            p = subprocess.run(args, text=True, capture_output=True, timeout=8)
            txt = (p.stdout or p.stderr).strip().splitlines()[:2]
            return path, " | ".join(txt)
        except Exception:
            pass
    return path, "found"

def main():
    report = {
        "python": sys.version,
        "platform": platform.platform(),
        "modules": {},
        "commands": {},
        "summary": {},
    }
    print("Python:", sys.version.split()[0])
    print("Platform:", platform.platform())

    missing_required = []
    print("\nPython modules:")
    for cat, mods in CATEGORIES.items():
        print(f"\n[{cat}]")
        report["modules"][cat] = {}
        for m in mods:
            ok = has_module(m)
            report["modules"][cat][m] = ok
            print(f"  {m:28s} {'OK' if ok else 'MISSING'}")
            if cat in {"core_python", "cheminformatics", "structure_biology", "simulation"} and not ok:
                missing_required.append(m)

    missing_cmds = []
    print("\nExecutables:")
    for cat, cmds in COMMANDS.items():
        print(f"\n[{cat}]")
        report["commands"][cat] = {}
        for c in cmds:
            path, ver = cmd_version(c)
            report["commands"][cat][c] = {"path": path, "version": ver}
            print(f"  {c:28s} {path or 'MISSING'}")
            if cat == "docking" and c in {"vina", "obabel"} and not path:
                missing_cmds.append(c)

    ok = not missing_required and not missing_cmds
    report["summary"] = {
        "ready_for_real_docking": ok,
        "missing_required_modules": missing_required,
        "missing_required_commands": missing_cmds,
        "note": "Some optional advanced tools may be missing without blocking core docking.",
    }
    print("\nSummary:")
    print(json.dumps(report["summary"], indent=2))
    with open("full_stack_verification.json", "w") as f:
        json.dump(report, f, indent=2)
    print("Wrote full_stack_verification.json")
    raise SystemExit(0 if ok else 1)

if __name__ == "__main__":
    main()
