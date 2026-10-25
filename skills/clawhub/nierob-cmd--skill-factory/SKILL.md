---
name: skill-factory
description: Design, build, evaluate, and optimize production-ready Agent Skills for ClawHub. Use when creating a new skill, redesigning an existing skill, choosing between a single skill, references/scripts, or a router with variants, improving skill triggers, validating portability, or preparing a skill for publication. Also use when turning a rough skill idea into a self-contained, publishable skill package.
---

# Skill Factory

A universal engineering workflow for creating high-quality Agent Skills intended for reuse and publication.

The factory chooses the simplest architecture that reliably solves the requested problem. A router + variants is one option, not the default.

## Core principle

Build the smallest self-contained skill that solves the real task, then validate it as if an unknown user installed it.

Do not add architecture merely because it is available.

## When to use

Use this skill when the user wants to:

- create a new Agent Skill;
- redesign or improve an existing skill;
- turn a rough idea into a reusable skill;
- choose an appropriate skill architecture;
- improve triggering and discovery;
- add references, scripts, or other supporting files;
- evaluate a skill before publication;
- prepare a skill for ClawHub publication.

## When not to use

Do not use this as the primary workflow when:

- the user only wants to execute an existing skill;
- the task is ordinary coding with no Agent Skill deliverable;
- the user only wants a security audit of an unrelated skill;
- the user only wants to publish an already validated skill and no changes are required.

## Workflow

### Step 1 — Understand the capability

Extract:

1. Purpose — what capability should the skill provide?
2. Users — who is expected to use it?
3. Inputs — what can the user provide?
4. Outputs — what should the skill produce?
5. Tools — which tools are actually required?
6. Constraints — environment, OS, dependencies, permissions, APIs.
7. Failure conditions — what should happen when information or prerequisites are missing?
8. Trigger boundary — when should the skill activate, and when should it stay out of the way?

Ask only the minimum questions required. If the user explicitly says to proceed, make reasonable assumptions and mark them.

### Step 2 — Choose the simplest architecture

Select one:

#### A. Single skill

Use for one coherent workflow with limited branching.

#### B. Skill + references

Use when the core workflow is stable but detailed domain knowledge, examples, schemas, or long instructions would unnecessarily inflate `SKILL.md`.

#### C. Skill + scripts

Use when deterministic computation, transformation, parsing, validation, or repeatable tool work is better implemented as code.

#### D. Router + variants

Use when there are 2–6 clearly distinguishable variants with materially different procedures.

Routing must be based on observable signals such as file type, explicit user intent, operation, domain, or other hard evidence.

#### E. Skill family

Use when multiple independently useful skills share a domain but should remain separately invocable.

Do not force unrelated capabilities into one skill.

### Step 3 — Design the skill contract

Define:

- name;
- concise description;
- intended triggers;
- non-triggers;
- inputs;
- outputs;
- workflow;
- tools and dependencies;
- assumptions;
- failure handling;
- safety boundaries;
- supported environments;
- supporting files;
- version.

The description is a contract. It must accurately disclose the capability and important trigger conditions. Do not hide major behavior in the body that a user or agent could not reasonably infer from the description.

### Step 4 — Write the core skill

Keep `SKILL.md` focused on the information needed during execution.

Prefer:

- clear headings;
- numbered procedures;
- explicit decision points;
- concise examples only when they clarify behavior;
- progressive disclosure;
- references for long material;
- scripts for deterministic operations.

Avoid:

- unnecessary background;
- repeated instructions;
- giant example collections;
- personal paths, usernames, secrets, or machine-specific assumptions;
- undocumented dependencies;
- instructions that exist only to impress the reader.

For a router family, every variant must remain independently understandable and directly invocable.

### Step 5 — Add supporting files only when justified

Use:

- `references/` for detailed knowledge that is useful but not needed on every invocation;
- `scripts/` for deterministic/repeatable computation or transformations;
- `assets/` only for actual runtime assets.

Every supporting file must have a clear purpose and be reachable from `SKILL.md`.

### Step 6 — Build trigger evaluations

Before calling the skill publish-ready, create a small realistic evaluation set.

Minimum recommended set:

- 8 positive cases;
- 8 hard-negative cases;
- 4 borderline cases;
- 2 adversarial/confusing cases.

Positive cases should represent realistic user requests, not trivial keyword matches.

Hard negatives should look plausible but belong to another capability.

For each case determine:

- should trigger?;
- expected skill/variant;
- why;
- observed result;
- correction required.

Tune the description and trigger wording against these cases.

### Step 7 — Validate execution quality

Check:

- Does the workflow actually solve the stated task?
- Are required inputs explicit?
- Are missing inputs handled?
- Are tools used only when needed?
- Are outputs deterministic enough for the task?
- Are instructions ordered correctly?
- Can an unfamiliar user understand the skill without prior conversation?

For variant families, additionally verify that each variant can be invoked directly.

### Step 8 — Validate portability

Pretend the skill was installed by an unknown user on an unknown compatible environment.

Look for:

- hard-coded usernames;
- personal directories;
- local-only file paths;
- assumptions about installed binaries;
- shell-specific syntax;
- undocumented environment variables;
- model-specific behavior;
- unavailable tools;
- credentials assumed to exist;
- network access that was not disclosed.

Either remove the dependency or document it clearly.

### Step 9 — Run a security and trust check

Inspect the complete package for:

- secrets or tokens;
- credential harvesting;
- unexpected network calls;
- destructive commands;
- unexplained downloads;
- hidden instructions;
- prompt-injection patterns;
- unnecessary filesystem access;
- unnecessary privilege requirements;
- suspicious obfuscation.

Do not silently remove behavior that is essential to the requested capability. Flag it and explain the risk.

### Step 10 — Run the publication quality gate

Before declaring the skill publish-ready, verify:

- [ ] valid `SKILL.md`;
- [ ] valid frontmatter;
- [ ] clear, accurate description;
- [ ] activation boundary is understandable;
- [ ] non-trigger cases are considered;
- [ ] instructions are self-contained;
- [ ] progressive disclosure is used where useful;
- [ ] supporting files are necessary and referenced;
- [ ] no personal or secret data;
- [ ] dependencies are disclosed;
- [ ] portability checked;
- [ ] security checked;
- [ ] trigger evaluation completed;
- [ ] realistic positive and hard-negative cases pass;
- [ ] package is self-contained;
- [ ] no unnecessary architecture;
- [ ] version/changelog is ready.

Only then report:

`PUBLISH-READY`

If a blocker remains, report:

`NOT READY`

and list the blockers.

## Router + variant rules

When a router architecture is selected:

1. Use only when there are 2–6 bounded variants.
2. Define deterministic recognition signals.
3. Make the routing table explicit.
4. Keep each variant independently invocable.
5. Give each variant its own trigger description.
6. Keep variant-specific rules inside the variant.
7. Do not make a variant depend on the router having been invoked first.
8. If the input cannot be classified reliably, ask for clarification or use a safe fallback.
9. Test the router with hard negatives and ambiguous cases.

## Updating an existing skill

When improving an existing published skill:

- preserve its public identity unless the user explicitly requests a new skill;
- do not casually rename the directory or frontmatter `name`;
- identify what changed and why;
- preserve working behavior unless there is a reason to change it;
- add regression cases for previously working behavior;
- increment the version according to the scope of the change;
- provide a concise changelog.

## Output

When the user asks to build a skill, produce:

1. the complete skill package;
2. a short architecture decision;
3. the validation result;
4. known limitations or assumptions;
5. publication metadata when requested.

Do not claim a skill is publish-ready if the quality gate was not actually checked.

## Anti-overengineering rule

Prefer:

`one coherent task → one skill`

`large knowledge → references`

`deterministic repeated work → scripts`

`2–6 materially different modes → router + variants`

`unrelated capabilities → separate skills`

The goal is reliability and reuse, not maximum file count.

## Reference

For the rationale behind architecture selection, trigger evaluation, progressive disclosure, portability, and publication quality, see:

`references/skill-mechanics.md`
