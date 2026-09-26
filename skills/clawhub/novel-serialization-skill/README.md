# GitHub Novel Serialization Skill

> **AI-Assisted Novel Serialization Skill** — A modular, harness-engineered system for writing, managing, and publishing serialized novels on GitHub.

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](LICENSE)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License--Novel%20Content-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSES/CC-BY-NC-SA-4.0.txt)
[![Skill Version](https://img.shields.io/badge/Skill%20Version-1.1.2-orange)](SKILL.md)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

---

## Overview

**github-novel-serialization-skill** is a production-grade, modular Skill that orchestrates AI-assisted novel writing and GitHub-based serialization. It covers the full creative lifecycle: **world-building -> character design -> chapter drafting -> continuity verification -> GitHub publishing**. Built on harness-engineering principles (constraint-before-generation, structured memory, verification gates, modular decomposition, and feedback loops), this Skill transforms a raw LLM into a reliable, stateful, multi-session novel-writing agent.

Every module is independently usable, composable, and under 500 lines — designed for compatibility with any LLM-backed coding agent (Claude Code, GitHub Copilot, Cursor, etc.).

---

## Architecture

```
+------------------------------------------------------------------+
|                        SKILL.md (Index)                          |
|  Overview | Output Language | Quick Start | Module Index         |
|  Workflow Pipeline | Quick Refs | Verification Gates             |
+----------------------+-------------------------------------------+
                       | references
                       v
+------------------------------------------------------------------+
|                     references/                                  |
|  method-patterns.md (master) | glossary.md | examples/           |
+----------------------+-------------------------------------------+
                       | modules
                       v
+------------------------------------------------------------------+
|                      modules/                                    |
|  +---------------+ +---------------+ +---------------+           |
|  | worldbuilding | | character-    | | chapter-      |           |
|  |               | | design        | | writing       |           |
|  +---------------+ +---------------+ +---------------+           |
|  +---------------+ +---------------+ +---------------+           |
|  | continuity-   | | publishing-   | | continuity-   |           |
|  | check         | | workflow      | | tracker       |           |
|  +---------------+ +---------------+ +---------------+           |
+------------------------------------------------------------------+
                       |
                       v
+------------------------------------------------------------------+
|                      prompts/                                    |
|  README.md | 01-implement-method.md | 02-robustness-checks.md    |
+------------------------------------------------------------------+
```

> **Note:** The architecture diagram above shows the logical layering of the Skill (progressive disclosure): SKILL.md (index) → references/ (templates) → modules/ (functional sub-skills) → prompts/ (human copy-paste templates). In the file system, `references/`, `modules/`, and `prompts/` are peer directories under the project root.

---

## Quick Start

### Step 1 — Clone the Skill

```
git clone https://github.com/[OWNER]/github-novel-serialization-skill.git
cd github-novel-serialization-skill
```

### Step 2 — Install into Your Agent

Add the Skill to your agent's skills directory:

#### For Claude Code

```
ln -s $(pwd) ~/.claude/skills/github-novel-serialization-skill
```

#### For GitHub Copilot / Cursor / Other Agents

```
# Copy the repo into your agent's skills directory
# Note: The skills directory path varies by agent. Consult your agent's documentation
# for the correct skills directory location. Common paths include:
#   - Claude Code: ~/.claude/skills/
#   - Cursor: check Cursor settings for custom skills directory
#   - Other agents: refer to their respective documentation
cp -r . <AGENT_SKILLS_DIR>/github-novel-serialization-skill
```

### Step 3 — Start Writing

Open your AI chat window and use any trigger phrase:

| Action | Prompt Example |
|--------|---------------|
| Build a world | "Build a world with magic systems and feudal politics" |
| Create characters | "Create a protagonist with a tragic backstory" |
| Write a chapter | "Write Chapter 1: The Awakening" |
| Check continuity | "Check continuity across all chapters" |
| Publish | "Publish chapter 1 as release v1.0" |

---

## Directory Structure

```
github-novel-serialization-skill/
|
+-- README.md                           # This file
+-- README FOR AI.md                    # Meta-instructions for AI generation (seed file)
+-- README_FOR_AI_Audit_Report.md       # Post-generation compliance audit report (Round 1)
+-- README_FOR_AI_Audit_Report_Round2.md # Content-level re-audit report (Round 2)
+-- README_FOR_AI_Audit_Report_Round3.md # Cross-document consistency audit (Round 3)
+-- .gitattributes                      # Line-ending policy (LF everywhere)
+-- SKILL.md                            # Index + quick-reference
+-- .gitignore                          # Git ignore rules
+-- .editorconfig                       # Editor configuration
+-- LICENSE                             # GPL-3.0
+-- LICENSES/                           # Additional licenses
|   +-- CC-BY-NC-SA-4.0.txt
+-- CODE_OF_CONDUCT.md                  # Community standards
+-- CONTRIBUTING.md                     # Contribution guidelines
+-- SECURITY.md                         # Security policy
+-- CHANGELOG.md                        # Version history
|
+-- references/                         # Deep documentation & templates
|   +-- method-patterns.md              # Master template file
|   +-- method-patterns-worldbuilding.md
|   +-- method-patterns-character.md
|   +-- method-patterns-chapter.md
|   +-- method-patterns-continuity.md
|   +-- method-patterns-publishing.md
|   +-- glossary.md
|   +-- examples/                       # Worked examples
|   |   +-- example-worldbuilding.md
|   |   +-- example-character-sheet.md
|   |   +-- example-chapter-draft.md
|
+-- prompts/                            # Dual-mode prompt templates (human copy-paste)
|   +-- README.md
|   +-- 01-implement-method.md
|   +-- 02-robustness-checks.md
|
+-- modules/                            # Functional sub-skills
|   +-- worldbuilding/
|   |   +-- SKILL.md
|   +-- character-design/
|   |   +-- SKILL.md
|   +-- chapter-writing/
|   |   +-- SKILL.md
|   +-- continuity-check/
|   |   +-- SKILL.md
|   +-- publishing-workflow/
|   |   +-- SKILL.md
|   +-- continuity-tracker/
|       +-- SKILL.md
|
+-- .github/                            # GitHub community health files
    +-- ISSUE_TEMPLATE/
    |   +-- bug-report.yml
    |   +-- feature-request.yml
    |   +-- config.yml
    +-- PULL_REQUEST_TEMPLATE.md
    +-- FUNDING.yml
    +-- dependabot.yml
    +-- workflows/
        +-- novel-release.yml
```

---

## Modules

| Module | Purpose |
|--------|---------|
| **worldbuilding** | Generate and maintain world-building documents (magic systems, geography, politics, culture) |
| **character-design** | Generate and maintain character sheets (identity, psychology, arcs, relationships, voice profiles) |
| **chapter-writing** | Draft chapters following established style guides and continuity constraints |
| **continuity-check** | Verify consistency across all chapters and state files (plot holes, timeline errors) |
| **publishing-workflow** | Manage Git-based publishing pipeline (tagging, releases, automated checks) |
| **continuity-tracker** | Maintain persistent state files (timeline, character states, thread ledger) |

---

## Installation

### For GitHub Skills

Add the Skill to your GitHub repository's skills directory:

```
# Clone the repository into your project's .github/skills directory
mkdir -p .github/skills
git clone https://github.com/[OWNER]/github-novel-serialization-skill.git .github/skills/github-novel-serialization-skill
```

### For Claude Code

```
# Clone the repository
git clone https://github.com/[OWNER]/github-novel-serialization-skill.git
cd github-novel-serialization-skill

# Create a symlink in your Claude Code skills directory
mkdir -p ~/.claude/skills
ln -s $(pwd) ~/.claude/skills/github-novel-serialization-skill
```

### For Cursor / Other Agents

```
# Clone the repository
git clone https://github.com/[OWNER]/github-novel-serialization-skill.git
cd github-novel-serialization-skill

# Copy the repository into your agent's skills directory
# Note: The skills directory path varies by agent. Consult your agent's documentation
# for the correct skills directory location. Common paths include:
#   - Claude Code: ~/.claude/skills/
#   - Cursor: check Cursor settings for custom skills directory
#   - Other agents: refer to their respective documentation
cp -r github-novel-serialization-skill <AGENT_SKILLS_DIR>/github-novel-serialization-skill
```

---

## Usage Examples

### Example 1: Build a World

Use the prompt template in `prompts/01-implement-method.md`:

```
You are a professional novel architect. Build a world for a:
- Genre: {{GENRE}} (e.g., "high fantasy")
- Setting: {{SETTING}} (e.g., "a archipelago of floating islands")
- Themes: {{THEMES}} (e.g., "power, corruption, redemption")
- Target chapters: {{TARGET_CHAPTERS}} (e.g., 50)
- Tone: {{TONE}} (e.g., "grimdark")
- POV style: {{POV_STYLE}} (e.g., "third-person limited")

Output everything in: {{OUTPUT_LANGUAGE}}
```

### Example 2: Check Continuity

Use the prompt template in `prompts/02-robustness-checks.md`:

```
Review the following chapter draft for:
1. Continuity consistency (character names, locations, timeline)
2. Style consistency (voice, tense, register)
3. Plot logic (causality, motivation, foreshadowing payoff)
4. Pacing analysis (scene-to-sequel ratio, tension curve)
5. Dialogue authenticity (voice differentiation per character)

Output a structured report with severity levels (Critical / Warning / Suggestion).
```

### Example 3: Publish a Release

```
# Tag a release
git tag -a v1.0.0 -m "Release v1.0.0: Chapters 1-5"
git push origin v1.0.0

# The GitHub Actions workflow will:
# 1. Validate chapter file formats
# 2. Verify license compliance
# 3. Run continuity checks
# 4. Create a GitHub Release with release notes
```

---

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before submitting pull requests.

- **Bug Reports**: [Open an Issue](https://github.com/[OWNER]/github-novel-serialization-skill/issues/new?template=bug-report.yml)
- **Feature Requests**: [Open a Feature Request](https://github.com/[OWNER]/github-novel-serialization-skill/issues/new?template=feature-request.yml)
- **Security Issues**: [View Security Policy](SECURITY.md)
- **Pull Requests**: Follow our branch naming and commit format conventions

---

## License

This project uses a **dual-licensing** model:

| Component | License |
|-----------|---------|
| **Skill Infrastructure** (code, templates, prompts, SKILL.md files, GitHub workflows, configuration files) | [GNU General Public License v3.0 (GPL-3.0)](LICENSE) |
| **Generated Novel Content** (chapters, character sheets, world-building docs) | [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](LICENSES/CC-BY-NC-SA-4.0.txt) |

See the [LICENSE](LICENSE) file for full GPL-3.0 terms and the [LICENSES/CC-BY-NC-SA-4.0.txt](LICENSES/CC-BY-NC-SA-4.0.txt) file for full CC BY-NC-SA 4.0 terms.

---

## Credits

- Built with principles from Harness Engineering
- Inspired by the [Keep a Changelog](https://keepachangelog.com/) and [Semantic Versioning](https://semver.org/) standards
- Community-driven project — built by and for novelists, writers, and AI enthusiasts

---

> **Note**: This Skill project is a harness-engineered system, not just a collection of prompts. Every file exists to constrain, guide, and verify — the goal is deterministic quality, not lucky outputs.
