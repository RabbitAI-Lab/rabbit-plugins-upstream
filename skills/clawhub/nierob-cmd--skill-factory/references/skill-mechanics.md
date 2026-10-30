# Skill Mechanics

This reference explains the reasoning behind the Skill Factory rules. Load it when designing or reviewing a skill; do not copy the entire reference into every generated `SKILL.md`.

## 1. Skill as a contract

A skill has two audiences:

1. the agent deciding whether the skill is relevant;
2. the agent executing the instructions after activation.

The frontmatter description therefore acts as a discovery contract. It should say what the skill does and the kinds of requests that should activate it. The body contains the execution procedure.

A useful test is:

> Could a user understand the capability and activation boundary from the description alone?

If not, improve the description rather than hiding the missing information in the body.

## 2. Architecture follows task shape

Do not choose a router because the factory can create one.

Use the smallest structure that keeps execution clear:

- one workflow → single skill;
- large supporting knowledge → references;
- deterministic repeated work → scripts;
- 2–6 distinct modes → router + variants;
- genuinely separate capabilities → skill family.

Extra layers create more discovery decisions, more maintenance, and more opportunities for inconsistent behavior.

## 3. Progressive disclosure

Put frequently needed execution instructions in `SKILL.md`.

Move large, stable, or rarely needed material into references.

Good candidates for references:

- detailed domain rules;
- long examples;
- schemas;
- compatibility matrices;
- troubleshooting;
- background rationale.

The main skill should tell the agent when and why to load each reference.

## 4. Trigger evaluation

A skill that is excellent after activation can still be poor if it activates at the wrong time.

Use realistic test prompts.

### Positive

Requests that should clearly use the skill.

### Hard negative

Requests that share vocabulary but require another capability.

### Borderline

Requests where the correct decision depends on context.

### Adversarial

Requests deliberately combining multiple intents or trying to push the skill outside its intended boundary.

The objective is not a perfect keyword match. It is a reliable activation boundary.

## 5. Self-contained execution

A published skill should not depend on the author's previous conversation.

Avoid:

- “as discussed earlier”;
- personal paths;
- undocumented project conventions;
- hidden files;
- unexplained environment variables;
- private APIs.

If an external dependency is necessary, document it.

## 6. Portability

A skill may be installed in environments different from the author's.

Prefer portable commands and explicit prerequisites.

When a platform-specific dependency is unavoidable, state:

- supported environment;
- required binary/package;
- required version where relevant;
- configuration needed;
- expected permissions.

## 7. Security and trust

A public skill should be understandable enough to audit.

Avoid unexplained:

- downloads;
- network requests;
- credential access;
- destructive commands;
- privilege escalation;
- obfuscated code.

If a capability genuinely needs one of these, make the behavior explicit and limit it to the minimum required scope.

## 8. Lack of surprise

The skill should behave in ways that a reasonable user would expect from its description.

Examples:

- A PDF-analysis skill should not silently modify unrelated files.
- A formatting skill should not upload documents to a remote service unless that behavior is disclosed and required.
- A router should not silently select a variant when the evidence is ambiguous.

When behavior could surprise the user, disclose it and prefer confirmation where appropriate.

## 9. Evaluation before publication

A publishable skill should have evidence that its trigger boundary and core workflow work.

The minimum recommended evaluation set is small by design. It is better to have realistic cases than dozens of trivial keyword examples.

Record failures and turn important failures into regression tests.

## 10. Versioning

Use semantic intent when practical:

- patch: fixes, wording, or non-behavioral corrections;
- minor: backward-compatible capabilities;
- major: changed public behavior, architecture, or compatibility expectations.

For a major redesign of the factory itself, use a major version.

## 11. Publication readiness

Before publication, inspect the whole package, not only `SKILL.md`.

A skill is publish-ready when:

- its identity is stable;
- its capability is clear;
- activation is bounded;
- execution is self-contained;
- dependencies are disclosed;
- supporting files are justified;
- portability and security have been reviewed;
- realistic evaluations have been considered;
- the package contains no author-specific secrets or assumptions.
