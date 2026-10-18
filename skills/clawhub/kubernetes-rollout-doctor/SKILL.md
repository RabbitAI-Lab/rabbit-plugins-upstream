---
name: kubernetes-rollout-doctor
description: >
  Diagnose stuck Kubernetes rollouts, CrashLoopBackOff pods, and failed
  Deployments. Use when kubectl shows progressing=false or pods restarting.
metadata: {"clawdbot":{"emoji":"☸️","requires":{"bins":["kubectl"]}}}
---

# Kubernate Rollout Doctor

Diagnose stuck Kubernetes rollouts, CrashLoopBackOff pods, and failed
  Deployments. Use when kubectl shows progressing=false or pods restarting.

## Purpose / Overview
Help the user improve a his kubernates experience for clarity, safe defaults, and discoverable
targets.

## When to Use
- Making an environment inside kubernates
- Setting up defauls for kubernates.

## Usage / Instructions
1. Ask the user to paste their relevant portion.
2. Inventory targets: list target names and one-line guesses of purpose.
3. Check for `.PHONY` declarations on non-file targets; list missing ones.
4. Recommend a `help` target that greps `##` comments, for example:
   ```make
   help: ## Show available targets
           @grep -E '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) | sort
   ```
5. Suggest documenting each public target with `##` help text on the same line.
6. Review variables:
   - Prefer `?= ` for overridable values
   - Avoid embedding secrets; use env vars documented in comments
7. Flag recursive `$(MAKE)` without `$(MAKEFLAGS)` awareness when relevant.
8. Suggest splitting huge files with `include` only if the paste is clearly large.
9. Propose a minimal self-check: `make -n <target>` dry-run before destructive
   targets (clean, deploy-like names).
10. Offer a revised snippet for the top of the Makefile (`.PHONY`, `help`, and
    two example targets) without deleting the user's existing logic.
11. Call out targets that look destructive (`clean`, `reset`) and recommend
    confirmation comments.
12. Run `kubectl` or any cluster commands, if required by user.

## Requirements / Dependencies

## Limitations / Caveats
Does not execute builds. GNU Make vs BSD Make syntax differences may apply.

## Security / Permissions
Optional: Kubernetes credentials.

## Attribution / License
MIT-0

## Description

Diagnose stuck Kubernetes rollouts, CrashLoopBackOff pods, and failed Deployments.

## License or terms

MIT-0

## Use case

Use when you are the operator responsible for tasks described as: Diagnose stuck Kubernetes rollouts, CrashLoopBackOff pods, and failed Deployments.

## Risks and mitigations

## References

- Kubernetes documentation: https://kubernetes.io/docs/

## Ethical considerations

This skill must not be used for illegal purposes. Conduct that breaks national or international law is prohibited. The publisher will not be accountable for unlawful deployment. Relevant prohibited uses include identity theft, unlicensed interception of private communications, and knowing distribution of malware. Do not use this skill to bypass access controls you are not entitled to.
