# ProPaymun Information Architecture

[![Version](https://img.shields.io/badge/version-1.0.1-5B4BDB)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT--0-2F855A)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-ready-111827)](SKILL.md)

Turn ordinary product context into clear, evidence-aware information architecture, product sitemaps, and user flows—even when the user does not know the terminology.

**ProPaymun** comes from the Persian «پروپیمان»: full and complete. Here, complete means decision-ready, understandable, and honest about uncertainty.

[فارسی](README.fa.md)

## Choose the right package

For one reusable file across file-capable chats, Projects, and Gemini Gems, use the [Workspace Kit Markdown](packages/workspace-kit/propaymun-ia-workspace-kit.md). Its opening section includes a short instruction to paste into the host. Native Claude Skills installation uses the ZIP instead. These distributions share one maintained IA method; the Markdown does not include executable helpers. Do not upload the Agent Skill ZIP to Gemini Knowledge.

The conversational workflow needs no tools. Optional bundled Python helpers validate IA, product-sitemap, or user-flow JSON, render IA HTML, or export builder specifications when requested. They use the standard library and do not access the network or credentials. Host permissions remain in force; installing the skill does not authorize file creation, persistent-memory changes, or script execution. Maintainer packaging tools are excluded from the installable ZIP. See [security scope and limitations](SECURITY.md).

| Package | Best for | Download |
|---|---|---|
| **Agent Skill Package** | Claude.ai Skills and only runtimes whose own documentation confirms compatible Agent Skill package support | [Download ZIP](packages/agent-skill/propaymun-information-architecture.zip) |
| **Workspace Kit** | ChatGPT Projects, Claude Projects, manually created Gemini Gems, and surfaces that provide persistent instructions plus file knowledge | [Knowledge file](packages/workspace-kit/propaymun-ia-workspace-kit.md) + [Workspace instructions](packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md) |

The two packages share the same canonical behavior. Automatic triggering, persistence, tools, and context limits still depend on the host product.

## Install in Claude.ai

1. Download the **[Agent Skill Package](packages/agent-skill/propaymun-information-architecture.zip)**.
2. In Claude.ai, enable **Settings → Capabilities → Code execution and file creation**.
3. Open **Customize → Skills**.
4. Choose **+ → Create skill → Upload a skill**.
5. Upload the ZIP without extracting it, then enable the skill.

A GitHub repository URL is not a Claude.ai upload package. Use the ZIP above.

## Configure a web workspace

For a workspace that explicitly provides both persistent instructions and file knowledge:

1. add [`propaymun-ia-workspace-kit.md`](packages/workspace-kit/propaymun-ia-workspace-kit.md) as project knowledge;
2. paste the short setup instruction from the Markdown file into the host's Instructions field; the separate [Workspace instructions](packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md) are an optional fuller alternative;
3. ask for information architecture, a product/UX sitemap, or a user flow in ordinary language.

This is configuration through project knowledge, not a claim of native Skill installation.

### Gemini web

Gemini web uses a manually created Gem rather than a native Skill installation:

1. choose **Explore Gems → New Gem**;
2. paste the short setup instruction from the Workspace Kit into the Gem instructions;
3. add [`propaymun-ia-workspace-kit.md`](packages/workspace-kit/propaymun-ia-workspace-kit.md) under **Knowledge**;
4. save the Gem.

### One-off file use

If a service only accepts files in a chat, attach the Workspace Kit and paste the short Workspace Instructions with the first message. This is session-scoped file use—not installation, persistent configuration, or guaranteed automatic triggering.

## Other Agent Skill runtimes

Use the Agent Skill Package only when the host's own documentation confirms this package format and installation route. This repository intentionally does not provide unverified CLI installation commands.

## Machine-scannable install map

```yaml
product: ProPaymun Information Architecture
skill_id: propaymun-information-architecture
canonical_entrypoint: SKILL.md
native_package: packages/agent-skill/propaymun-information-architecture.zip
native_package_verified_for: [claude.ai-skills]
workspace_knowledge: packages/workspace-kit/propaymun-ia-workspace-kit.md
workspace_instructions: packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md
workspace_requires: [persistent-instructions, file-knowledge]
gemini_web: create-a-new-gem-manually
one_off_file_use: attach-workspace-kit-and-paste-instructions
do_not_claim: [native-installation, persistent-behavior, automatic-triggering, unverified-cli-support]
package_manifest: packages/manifest.json
semantic_schema: schema/semantic-ia.schema.json
companion_schemas: [schema/product-sitemap.schema.json, schema/user-flow.schema.json]
visual_builder_exporter: scripts/export_builder_handoff.py
legacy_download_paths: preserved
release_state: v1.0.1
```

An AI installer should select exactly one host-appropriate package, preserve the package contents, and avoid claiming native installation when it only attached a knowledge file.

## What the skill does

- inspects the brief, attachments, conversation, and authorized sources before asking;
- reassesses sufficiency throughout the work instead of asking a fixed first-round questionnaire;
- asks only questions whose answers can change the next architecture decision, then stops by itself;
- infers whether the user needs orientation, idea exploration, a provisional structure, full IA, an audit, a focused product sitemap or user flow, or a downstream transformation;
- treats “I don’t know” as a mentoring signal: proposes one reversible starting point and continues without serial interrogation;
- translates structure into user, business, and operational consequences without requiring product or IA expertise;
- keeps persistent memory from silently changing the current scope, evidence, deliverable, or durable project context;
- manages context with compact deltas, progressive disclosure, and one representation at a time;
- separates language from locale, jurisdiction, culture, and operating model;
- recognizes content/taxonomy, object/operation, and hybrid IA problems before choosing model depth;
- models information domains, canonical items, hierarchy, typed relationships, taxonomy, labels, metadata, findability, access, lifecycle, and governance;
- separates provided facts, observations, confirmation, inference, proposals, conflicts, and unknowns;
- uses current public research when it can materially improve the IA and browsing is available;
- uses accepted IA as the semantic source for requested downstream work, while allowing a standalone product sitemap or stateful user flow to start from a versioned minimum semantic substrate;
- distinguishes a product/UX sitemap from an XML/SEO sitemap and chooses the artifact by decision purpose.

## How the adaptive workflow behaves

The user does not choose a mode or manage checkpoints.

```text
inspect context
→ model the next consequential layer
→ detect an architecture-changing unknown
→ complete safe independent work
→ ask the smallest useful question for the affected decision and stop
→ continue after the answer
→ verify handoff readiness before creating an artifact
```

As soon as the available context supports a responsible baseline, the skill gives one coherent useful pass instead of asking about every modeling layer separately. If the user does not know, it explains one reversible starting point in ordinary language and continues through a useful slice before asking again. Internal status codes remain in structured handoffs rather than novice-facing conversation. Alternatives appear only when they make the choice easier. It never turns language or cultural stereotypes into confirmed product rules or silently adds growth, registration, payment, or monetization commitments.

## From IA to the output you need

IA remains the source of truth, not the ceiling of the workflow. Once it is ready enough for the intended decision, an explicit request can turn it into a diagram, UI brief or image, prototype/build prompt, product sitemap, user flow, document/presentation, or technical mapping. Internally, the skill captures an **IA Reference Lock** for the approved structure, labels, findability, access/privacy, evidence, unresolved assumptions, and adaptation boundaries; the technical name appears only when a team or machine handoff needs it. A standalone sitemap or flow uses a smaller versioned semantic substrate instead of forcing complete IA discovery. If the current environment cannot directly produce the requested format, it returns a truthful self-contained handoff.

## Visual Builder Handoff

Figma Make, Lovable, and similar prompt-to-build tools are downstream environments, not the place where IA decisions are made. A handoff has one explicit intent: an **IA review blueprint** or a **product prototype constrained by the IA**.

After the IA is ready for its intended purpose, ask:

```text
Create a Visual Builder Handoff for Figma Make from this information architecture.
```

The handoff contains:

1. a self-contained Markdown build specification;
2. a short copy-ready launch instruction for the builder's text box.

This matters because long attached prompts may be treated as files while the Generate button still requires a short text instruction.

Deterministic export:

```bash
python scripts/export_builder_handoff.py path/to/ia.json --target figma-make --intent ia-blueprint -o build-spec.md
python scripts/export_builder_handoff.py path/to/ia.json --target lovable --intent product-prototype -o prototype-spec.md
```

For an IA blueprint, the primary view shows domain containers, mapped items, hierarchy, and labeled relationships. A product-prototype handoff instead asks the downstream builder to create an interface constrained by the IA; it does not display the internal IA map as the product.

## Semantic IA 2.0

The renderer-independent model lives at [`schema/semantic-ia.schema.json`](schema/semantic-ia.schema.json). It uses:

- explicit domain-to-item mapping;
- one canonical item registry;
- primary hierarchy plus typed relationships;
- separate roles and item-scoped permissions;
- structured lifecycle states and transitions;
- locale context with evidence state;
- explicit problem shape and priority information-need traces;
- handoff readiness and blocking unknowns.

Validate or render a model:

```bash
python scripts/validate_ia_model.py path/to/ia.json
python scripts/render_ia_html.py path/to/ia.json -o ia.html
```

## Repository map

```text
SKILL.md                     canonical behavior
agents/                      host-facing skill metadata
references/                  conditional IA operating guidance
schema/                      Semantic IA 2.0 contract
scripts/                     validation, rendering, packaging, and handoff export
packages/                    professional installable packages
install/                     compatibility aliases for previously shared links
evals/                       behavioral cases and rubric
tests/                       deterministic script and package tests
```

## Development and validation

```bash
python scripts/build_packages.py
python -m unittest discover -s tests -v
python /path/to/skill-creator/scripts/quick_validate.py .
```

GitHub Actions rebuilds the packages, verifies byte-for-byte parity, validates the semantic and companion-model fixtures, and runs the deterministic test suite. The cross-host evidence and release criteria are documented in [the 1.0 release gate](evals/RELEASE-GATE.md).

## Versioning and compatibility

The project uses Semantic Versioning and the [MIT No Attribution license](LICENSE). Version 1.0.0 is the first stable contract: end-to-end IA remains the core, with product-sitemap and stateful user-flow companions, portable file-only guidance, traceable downstream composition, and evidence-aware validation boundaries.

Previously shared `install/claude-ai` and `install/universal-web` URLs remain synchronized compatibility aliases. New documentation uses the professional package names above.
