# Dependency Issue Patterns — Quick Reference

## Proven Search Queries (tested 2026-06-02)

### By Error Type
```
gh search issues "ImportError" --label bug --state open --limit 10 --sort created
gh search issues "ModuleNotFoundError" --label bug --state open --limit 10 --sort created
gh search issues "\"cannot import\"" --label bug --state open --limit 10 --sort created
gh search issues "\"No module named\"" --state open --limit 10 --sort interactions
```

### By Conflict Type
```
gh search issues "\"version conflict\"" --label bug --state open --limit 10
gh search issues "\"incompatible\" \"dependency\"" --label bug --state open --limit 10
gh search issues "\"ResolutionImpossible\"" --state open --limit 15 --sort interactions
gh search issues "\"pip install\" \"conflict\"" --state open --limit 15 --sort interactions
gh search issues "\"cannot install\" \"requires\"" --state open --language python --limit 20
```

### By Label
```
gh search issues --label "dependencies" --state open --limit 30 --sort created
gh search issues --label "dependencies" --label bug --state open --language python --limit 20
```

### Broad Dependency Scan (catches most issues)
```
gh search issues "dependency" --state open --language python --limit 50 --sort created \
  --json repository,title,url,number,createdAt,author \
  --jq '.[] | select(.createdAt > "2026-05-25" and (.author.login | test("dependabot|renovate|bot") | not) and (.title | test("(?i)conflict|missing|incompatible|version|break|error|fail|install|require|extra|optional|pin|relax|constraint|upper|bound")))'
```

### Excluding Bot Authors
```
gh search issues "dependency" --state open --limit 50 --sort created \
  --json repository,title,url,number,createdAt,author \
  --jq '.[] | select(.createdAt > "2026-05-25" and (.author.login | test("dependabot|renovate|bot") | not))'
```

### Language-Agnostic
```
gh search issues "\"peer dep\"" --state open --label bug --limit 20
gh search issues "\"go.mod\" \"incompatible\"" --state open --limit 15
gh search issues "\"dependency\" \"conflict\" \"Cargo.toml\"" --state open --limit 15
gh search issues "\"Package.swift\" \"incompatible\"" --state open --language swift --limit 15
gh search issues "\"pubspec.yaml\" \"incompatible\"" --state open --language dart --limit 15
```

### Per-Ecosystem Hot Packages (most dependency conflicts)
- **Python**: numpy, scipy, protobuf, cryptography, pydantic-core, opencv-python-headless
- **Node**: zod, typescript, @types/node, chokidar, react
- **ML**: torch, tensorflow, transformers, vllm, numba-cuda
- **Swift**: swift-tools-version, Package.swift
- **Flutter/Dart**: flutter_secure_storage, drift, serverpod

## Real Examples Fixed

### 1. Module Rename (DataDog/dd-trace-py #18393 -> PR #18397)
- **Symptom**: `No module named 'vllm.v1.engine.processor'`
- **Cause**: vLLM 0.14.0 removed compat shim `processor.py` -> `input_processor.py`
- **Fix**: Runtime fallback import -- try new path, fall back to old
- **Key detail**: vLLM 0.13.0 had a `__getattr__` shim in processor.py that re-exported InputProcessor with deprecation warning. 0.14.0 removed it entirely.

### 2. Upper Bound Too Tight (deepgram/deepgram-python-sdk #701 -> PR #723)
- **Symptom**: `pydantic-core>=2.18.2,<2.44.0` incompatible with pydantic 2.13.3
- **Cause**: pydantic-core upper bound not updated for new pydantic releases
- **Fix**: Widen `<2.44.0` to `<3.0.0`
- **Key detail**: pydantic-core follows calver, not semver. API stable within major versions.

### 3. Exact Pin Conflict (scottbarnesg/smart-sec-cam #69 -> PR #79)
- **Symptom**: `numpy==1.24.2` vs `opencv-python-headless>=4.10` (requires numpy>=2)
- **Cause**: Exact numpy pin + opencv dropped numpy 1.x support
- **Fix**: `numpy==1.24.2` -> `numpy>=1.24.2`, bump requires-python to >=3.9
- **Key detail**: Raspberry Pi users may need `sudo apt upgrade python3-picamera2` if simplejpeg was compiled against numpy 1.x

### 4. Runtime Dep in devDeps (nexus-substrate/nexus-toolkit #11 -> PR #17)
- **Symptom**: `npm install nexus-toolkit` + import -> missing zod module
- **Cause**: `zod` in devDependencies but `src/types.ts` imports it at runtime, compiled into dist/
- **Fix**: Move zod from devDependencies to dependencies
- **Pattern**: Check `files` whitelist in package.json -- if it publishes dist/, runtime imports matter

### 5. Patch-Level Pin (AvaCodeSolutions/django-email-learning #500 -> PR #520)
- **Symptom**: `cryptography (>=48.0.0,<48.1.0)` conflicts with any system having >=48.1.0
- **Cause**: Over-tight patch-level upper bound
- **Fix**: Widen to `>=48.0.0,<49.0.0`
- **Pattern**: Patch-level pins are almost always wrong for open-source packages. Also had pillow, pydantic, pyjwt pinned similarly -- only fixed cryptography per issue scope.

### 6. Missing Type Definitions (nexus-substrate/memory-bench #8 -> PR #15)
- **Symptom**: `error TS2580: Cannot find name 'process'` on clean install
- **Cause**: `@types/node` only in pnpm-lock.yaml as optional peer dep of tsx/vitest, not guaranteed installed
- **Fix**: Add `@types/node: "^22.0.0"` to devDependencies
- **Key detail**: matches `engines.node >=22` in package.json

### 7. Missing in requirements.txt (imbus/testbench2robotframework #15 -> PR #16)
- **Symptom**: `pip install -r requirements.txt` -> missing click module
- **Cause**: `click` in pyproject.toml dependencies but not in pip-compile generated requirements.txt
- **Fix**: Add `click==8.4.1` to requirements.txt
- **Pattern**: pip-compile output drifts when pyproject.toml deps change without re-running pip-compile

### 8. Missing Extras (fastino-ai/GLiNER2 #111 -> PR #112)
- **Symptom**: `ERROR: gliner2 1.3.1 does not have an extra named 'local'`
- **Cause**: `[project.optional-dependencies]` section missing from pyproject.toml entirely
- **Fix**: Add the section with `local = ["torch", "transformers", "peft"]`
- **Pattern**: README/docs promise extras that pyproject.toml doesn't define. Check README install instructions vs actual pyproject.toml.

### 9. Runtime Type Import (pydantic/pydantic-settings #879 -> PR #880)
- **Symptom**: `types-boto3[secretsmanager]` required at runtime even though only used for type annotations
- **Cause**: `SecretsManagerClient` imported at runtime inside `import_aws_secrets_manager()` function, but only used in type annotation
- **Fix**: Move import under `TYPE_CHECKING` guard; remove from runtime import function
- **Key detail**: `from __future__ import annotations` already present makes type annotations lazy -- no runtime evaluation needed. Remove the type dep from `aws-secrets-manager` extras, keep it in `linting` group.

### 10. Build Tool Format Error (Scandit/scandit-capacitor-datacapture-core #9 -> PR #10)
- **Symptom**: Xcode SPM resolution fails when adding Capacitor package
- **Cause**: `import Foundation` on line 1 instead of `// swift-tools-version: 5.5`
- **Fix**: Move swift-tools-version comment to line 1 (SPM requires it as first line)
- **Pattern**: SPM Package.swift has strict format requirements. swift-tools-version MUST be the very first line.

## Pre-flight Checklist (before writing any code)

1. **Existing PRs?** -- `gh search prs --repo OWNER/REPO --state open` filtered for the issue
2. **Already fixed?** -- Check recent commits, maintainer comments on the issue
3. **Default branch?** -- `gh api repos/OWNER/REPO --jq '.default_branch'` (main vs master)
4. **Fork exists?** -- `gh repo view gavin913-lss/REPO --json name 2>&1` (check for "Could not resolve")

## Repos Already Checked (PRs exist or fixed)

- NVIDIA-NeMo/NeMo #15331 -- 2 PRs open (#15176, #15180)
- ronnnnnnnnnnnnn/etekcity_fitness_scale_ble #31 -- fixed in v0.4.6
- a-maliarov/amazoncaptcha #140 -- PR #153 open
- mkdocs/mkdocs #4032 -- PR #4111 open
- huggingface/transformers #46291 -- PR #46293 open
- redhat-developer/yaml-language-server #1264 -- PR #1267 open
- deezer/spleeter #917 -- PR #790 open (protobuf)
- cp2k/cp2k-output-tools #51 -- PR #56 open (regex upper bound)
- browser-use/browser-use #4824 -- PR #4882 open (relax pins)
- spacetelescope/pastasoss #19 -- PR #20 open (numpy 2.0+)
- CcgAlberta/pygeostat #139 -- PR #140 open (pandas 3.0)
- obynio/certbot-plugin-gandi #57 -- PR #56 open
- facebook/react #35758 -- fixed in eslint-plugin-react-hooks@7.1.1

### 11. Transitive Dependency Dropped (TheR1D/shell_gpt #771)
- **Symptom**: `ModuleNotFoundError: No module named 'click'` on clean install
- **Cause**: `click` imported directly in 5 files but not declared in dependencies. Was transitive via `typer`, but typer 0.26.7 dropped it.
- **Fix**: Add `click` to `[project] dependencies` in pyproject.toml
- **Key detail**: Always check if a transitive dependency is used directly in code. If `import click` appears, it must be a direct dependency.
- **Stars**: 12.1k (high-impact project)
- **Pattern**: typer dropping click is a common source of breakage across many projects.

### 12. Python Import Resolution Shadowing (ott-jax/ott #700 -> PR #701)
- **Symptom**: `AttributeError: module 'jax.interpreters.batching' has no attribute 'is_vmappable'`
- **Cause**: `from jax._src.interpreters import batching` resolves to the PUBLIC module (which re-exports from private), but the public module removed `is_vmappable` in JAX 0.9. The private submodule still has it.
- **Fix**: Change to `import jax._src.interpreters.batching as batching` — forces sys.modules lookup, bypasses public re-export.
- **Pattern**: When `from X.Y import Z` resolves to the wrong module due to package re-exports, use `import X.Y as Y` instead.
- **Stars**: ~500 (optimal transport library)

## PR Body Escaping

When PR body contains backticks, code blocks, or special chars, use `--body-file /tmp/body.md` instead of inline `--body`. Shell heredocs with nested backticks fail silently.
