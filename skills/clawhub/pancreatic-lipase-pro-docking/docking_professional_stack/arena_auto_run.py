#!/usr/bin/env python3
"""Arena one-command autorunner.

Goal: run real docking inside Arena.ai Agent Mode with no manual instructions.
It auto-detects an input CSV, attempts to install missing Python-level dependencies,
then runs the professional pancreatic lipase docking pipeline. It fails closed by
default: if real docking cannot run, it does NOT silently produce decision-grade dry
results. Use --allow-dry only for a report preview.

Usage:
  python arena_auto_run.py --input ligands.csv
  python arena_auto_run.py              # auto-detects a CSV in current folder
  python arena_auto_run.py --allow-dry  # preview only if docking tools cannot install
"""
from __future__ import annotations
import argparse, csv, importlib.util, os, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run(cmd, check=False, timeout=None, cwd=None):
    print('$', ' '.join(map(str, cmd)), flush=True)
    p = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout, cwd=cwd)
    if p.stdout: print(p.stdout[-4000:])
    if p.stderr: print(p.stderr[-4000:], file=sys.stderr)
    if check and p.returncode:
        raise SystemExit(p.returncode)
    return p


def has_module(m):
    return importlib.util.find_spec(m) is not None


def find_input(explicit=None):
    if explicit:
        p = Path(explicit)
        if not p.exists(): raise SystemExit(f'Input not found: {p}')
        return p.resolve()
    candidates = []
    for p in Path.cwd().glob('*.csv'):
        try:
            with p.open(newline='') as f:
                header = next(csv.reader(f), [])
            cols = {c.strip() for c in header}
            if {'smiles', 'SMILES', 'canonical_smiles'} & cols:
                candidates.append(p)
        except Exception:
            pass
    if not candidates:
        raise SystemExit('No ligand CSV found. Upload/provide a CSV with columns name,smiles.')
    if len(candidates) > 1:
        print('Multiple ligand CSV files found; using first:', candidates[0])
    return candidates[0].resolve()


def bootstrap():
    """Try to install the minimal Arena-compatible Python stack.

    Notes:
    - `vina` pip package provides both the Python module and the `vina` CLI binary
      on manylinux/macOS wheels; on systems without wheels it requires building
      against Boost and will fail (caught by can_real_dock).
    - `meeko` requires `gemmi` at import time (since 0.6+); install both.
    - `mk_prepare_receptor.py` is the Meeko receptor prep CLI.
    - Receptor prep still needs `mk_prepare_receptor.py` from Meeko; if unavailable,
      the pipeline will fail closed instead of fabricating docking results.
    """
    os.environ['PATH'] = str(Path.home()/'.local/bin') + os.pathsep + os.environ.get('PATH', '')
    missing_mods = [m for m in ['rdkit', 'meeko', 'vina', 'gemmi', 'pandas', 'numpy'] if not has_module(m)]
    missing_cmds = []
    if not shutil.which('vina'): missing_cmds.append('vina')
    if not (shutil.which('mk_prepare_receptor.py') or shutil.which('obabel')):
        missing_cmds.append('mk_prepare_receptor.py-or-obabel')
    if not missing_mods and not missing_cmds:
        print('Core docking dependencies already available.')
        return
    pkgs = ['rdkit', 'meeko', 'vina', 'gemmi', 'pandas', 'numpy', 'scipy', 'scikit-learn']
    # v101.0.5: this used to run unconditionally. `pip install --user --upgrade`
    # mutates the user's account-wide site-packages and can UPGRADE unrelated
    # existing installs — a persistent environment change the skill's own
    # documentation said it would not make. It is now strictly opt-in.
    if os.environ.get('HPL_ALLOW_PIP_BOOTSTRAP') != '1':
        print('Missing dependencies: ' + ', '.join(missing_mods + missing_cmds), file=sys.stderr)
        print('Refusing to auto-install: `pip install --user --upgrade` would modify your\n'
              'account-wide Python environment and may upgrade unrelated packages.\n'
              'Recommended (isolated, nothing global):\n'
              '  micromamba create -p plenv -c conda-forge python=3.11 rdkit meeko vina gemmi openbabel pytest\n'
              '  export PATH="$PWD/plenv/bin:$PATH"\n'
              'To opt in to the old behaviour anyway: HPL_ALLOW_PIP_BOOTSTRAP=1',
              file=sys.stderr)
        return
    print('HPL_ALLOW_PIP_BOOTSTRAP=1 set — running pip --user bootstrap...')
    cmd = [sys.executable, '-m', 'pip', 'install', '--user', '--upgrade'] + pkgs
    p = run(cmd, check=False, timeout=1200)
    os.environ['PATH'] = str(Path.home()/'.local/bin') + os.pathsep + os.environ.get('PATH', '')
    if p.returncode:
        print('Automatic pip bootstrap failed. Real docking may not be possible in this sandbox.',
              file=sys.stderr)
        print('  (Common cause: no prebuilt Vina wheel for this platform; needs Boost/CMake.)',
              file=sys.stderr)


def can_real_dock():
    os.environ['PATH'] = str(Path.home()/'.local/bin') + os.pathsep + os.environ.get('PATH', '')
    vina_ok = bool(shutil.which('vina'))
    ligand_ok = has_module('rdkit') and has_module('meeko')
    receptor_ok = bool(shutil.which('mk_prepare_receptor.py') or shutil.which('obabel'))
    return (vina_ok and ligand_ok and receptor_ok,
            {'vina_cli': shutil.which('vina'),
             'rdkit': has_module('rdkit'),
             'meeko': has_module('meeko'),
             'gemmi': has_module('gemmi'),
             'receptor_prep': (shutil.which('mk_prepare_receptor.py') or shutil.which('obabel'))})


def main():
    ap = argparse.ArgumentParser(description='Professional pancreatic lipase docking auto-runner.')
    ap.add_argument('--input', help='CSV of ligands (columns name,smiles[,reference_ic50_um,notes])')
    ap.add_argument('--out', default=None, help='Output CSV path (default: speed_runs/<run-id>/final_ranked_results.csv)')
    ap.add_argument('--poses', default=None, help='Directory for docked pose PDBQTs (default: inside speed_runs/<run-id>/dock/)')
    ap.add_argument('--allow-dry', action='store_true',
                    help='allow dry preview if dependencies cannot be installed')
    ap.add_argument('--quality', default='standard', choices=['screen', 'standard', 'high', 'ultra'])
    ap.add_argument('--engine', default='multi', choices=['multi', 'classic'],
                    help="multi = v100.4 5-site engine (chemprep protonation/tautomer/stereo, "
                         "complex receptor lipase+colipase+Ca, replicate seeds, native-ligand gate). "
                         "classic = legacy speed pipeline.")
    ap.add_argument('--exhaustiveness', type=int, default=None,
                    help='Vina exhaustiveness (overrides --quality preset; screen=4, standard=8, high=16, ultra=32)')
    ap.add_argument('--n-poses', type=int, default=None, help='number of poses per ligand (default: Vina default 9)')
    ap.add_argument('--cpu', type=int, default=min(8, max(1, os.cpu_count() or 1)),
                    help='total Vina threads (capped at 8 by default)')
    ap.add_argument('--cpu-per-dock', type=int, default=1, help='threads per parallel Vina worker')
    ap.add_argument('--workers', type=int, default=None, help='parallel Vina workers (default: cpu/cpu-per-dock)')
    ap.add_argument('--seed', type=int, default=42, help='random seed for reproducibility')
    ap.add_argument('--prefilter', choices=['none', 'all_valid', 'druglike', 'strict'], default='all_valid')
    ap.add_argument('--gi-mode', choices=['off', 'intestinal', 'strict'], default='intestinal')
    ap.add_argument('--run-id', default=None, help='explicit run-id (default: timestamped)')
    ap.add_argument('--limit', type=int, default=None, help='only dock first N ligands (debugging)')
    args = ap.parse_args()

    inp = find_input(args.input)
    print('Input:', inp)

    # First try bootstrap so that linter tool-check sees post-install state;
    # linter warnings are advisory (we call with check=False).
    bootstrap()
    run([sys.executable, str(HERE/'workflow_linter.py'), '--ligands', str(inp), '--check-tools'], check=False)

    ok, status = can_real_dock()
    print('Dependency status:', status)
    mode = 'dock' if ok else 'dry'
    if not ok and not args.allow_dry:
        raise SystemExit(
            'Real docking dependencies are still unavailable after auto-bootstrap. '
            'Refusing dry-mode output. Re-run with --allow-dry only for a non-docking preview.')

    if args.engine == 'multi' and mode == 'dock':
        tier = {'screen': 'fast', 'standard': 'balanced', 'high': 'balanced', 'ultra': 'max'}[args.quality]
        outdir = Path.cwd() / 'speed_runs' / (args.run_id or f"multi_{args.quality}")
        cmd = [sys.executable, str(HERE/'multi_site_docking.py'),
               '--ligands', str(inp),
               '--precision', tier,
               '--outdir', str(outdir),
               '--workers', str(args.workers or max(1, args.cpu // max(1, args.cpu_per_dock))),
               '--cpu-per-dock', str(args.cpu_per_dock),
               '--seed', str(args.seed)]
        if args.exhaustiveness is not None:
            cmd += ['--exhaustiveness', str(args.exhaustiveness)]
        if args.n_poses is not None:
            cmd += ['--n-poses', str(args.n_poses)]
        if args.limit is not None:
            cmd += ['--limit', str(args.limit)]
        run(cmd, check=True, timeout=None)
        run([sys.executable, str(HERE/'validate_results.py'), '--results',
             str(outdir/'results_all_sites.csv')], check=False)
        print('Results CSV   :', outdir/'results_all_sites.csv')
        print('Detail rows   :', outdir/'runs_detail.csv')
        print('Protocol gate : python3 validate_native.py  (MUP re-dock RMSD <= 2 A)')
        return

    cmd = [sys.executable, str(HERE/'docking_speed_pipeline.py'),
           '--input', str(inp),
           '--target-pdb', '1LPB',
           '--mode', mode,
           '--quality', args.quality,
           '--total-cpu', str(args.cpu),
           '--cpu-per-dock', str(args.cpu_per_dock),
           '--gi-mode', args.gi_mode,
           '--prefilter', args.prefilter,
           '--executive-dashboard']
    if args.exhaustiveness is not None:
        cmd += ['--exhaustiveness', str(args.exhaustiveness)]
    if args.workers is not None:
        cmd += ['--workers', str(args.workers)]
    if args.limit is not None:
        cmd += ['--limit', str(args.limit)]
    if args.run_id is not None:
        cmd += ['--run-id', args.run_id]
    # Seed: expose via VINA_SEED env and pass through to exhaustiveness-related code.
    # (The underlying pipeline uses deterministic default worker scheduling; seed is
    # applied to Vina via the VINA_SEED environment variable honored by Vina 1.2+.)
    os.environ['VINA_SEED'] = str(args.seed)
    # Note: docking_speed_pipeline doesn't currently accept a --seed flag; we pass it
    # as environment so it's available if Vina honors it. If the underlying script is
    # extended to add a --seed flag, add `cmd += ['--seed', str(args.seed)]` here.

    run(cmd, check=True, timeout=None)

    # Find latest run directory
    runs_dir = Path.cwd() / 'speed_runs'
    if not runs_dir.exists():
        raise SystemExit(f'Expected {runs_dir} to exist after docking run — something went wrong.')
    latest = sorted(runs_dir.glob('*'), key=lambda p: p.stat().st_mtime, reverse=True)[0]
    print('Latest run:', latest)

    results_csv = latest / 'final_ranked_results.csv'
    if args.out:
        out = Path(args.out).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(results_csv, out)
        print('Copied results ->', out)
        results_csv = out

    if mode == 'dock':
        run([sys.executable, str(HERE/'validate_docking_outputs.py'), '--run-dir', str(latest)], check=False)
    print('Main dashboard:', latest/'executive_dashboard.html')
    print('Results CSV   :', results_csv)
    print('Docked poses  :', latest/'dock/')


if __name__ == '__main__':
    main()
