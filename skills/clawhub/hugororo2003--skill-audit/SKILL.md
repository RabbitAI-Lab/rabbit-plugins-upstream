---
name: skill-audit
description: Audit any agent skill (SKILL.md) for quality, structure and prompt-injection / security risks before installing or publishing it. Use when the user wants to vet, review, score or compare skills, or before installing any third-party skill from ClawHub, skills.sh or GitHub. Produces a scored report card and a badge.
license: MIT
---

## When to use
- The user is about to install or run a skill from a marketplace or an unknown repo.
- The user asks to review, score, compare or rank skills.
- You are publishing a skill and want a pre-flight quality check.

## Procedure
1. Locate the target: a directory containing SKILL.md, a single SKILL.md file, or a cloned repo.
2. Run the auditor:
   - If running locally from the skill-audit directory:
     ```bash
     node bin/cli.js <path-to-skill> --out reports/
     ```
   - Or running directly via GitHub:
     ```bash
     npx github:hugororo2003/skill-audit <path-to-skill> --out reports/
     ```
3. Read the report in this order:
   - SAFETY findings (S*, R*): any FAIL means do not install; explain the risk to the user.
   - STRUCTURE (T*), CLARITY (C*), MAINTAINABILITY (M*): quality issues.
4. Give the user a verdict: score, grade, and install / do-not-install recommendation.
5. Optionally share the HTML report card from reports/ and the badge line for their README.

## Notes
- Exit code 1 = at least one critical finding (CI-friendly).
- Auditing is static and offline: nothing in the target skill is executed.
