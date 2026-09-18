# Freshness, Open Source, and Portability

## Contents

- [Purpose](#purpose)
- [First inspect the project](#first-inspect-the-project)
- [Current evidence requirement](#current-evidence-requirement)
- [Selection order](#selection-order)
- [Build-versus-adopt gate](#build-versus-adopt-gate)
- [Portability contract](#portability-contract)
- [Dependency decision record](#dependency-decision-record)
- [User-requested provider](#user-requested-provider)
- [Do not chase fashion](#do-not-chase-fashion)


## Purpose

Prevent outdated stack choices, unnecessary custom systems, and avoidable platform lock-in.

Inherit the parent baseline, target capability, guardrails, intended environment, and required evidence state. A newer dependency is not progress unless it measurably closes that target gap.

Apply this protocol whenever the task introduces or materially changes a framework, library, API, service, protocol, database, build tool, component system, agent framework, or deployment pattern.

## First inspect the project

Before recommending anything new, inspect:

- package manifests and lockfiles
- framework and runtime versions
- existing design system and utilities
- architecture decisions and project instructions
- supported deployment targets
- language and team conventions
- tests and build tooling

Prefer a fit existing dependency over introducing a competing abstraction.

## Current evidence requirement

Do not select technology from model memory alone.

When browsing or repository access is available, verify from primary sources:

- current official documentation
- current stable release or support line
- changelog or release notes
- repository ownership and maintenance signals
- package registry metadata
- license
- runtime and framework compatibility
- security notices or deprecation status
- migration guidance

Record the date checked and source.

A lack of recent releases is a warning, not automatic rejection, for mature stable software. Look for unresolved maintenance, compatibility, security, or governance risk rather than rewarding release frequency by itself.

If current verification is unavailable, avoid claiming that a choice is current. Prefer the existing project stack or present the decision as blocked.

## Selection order

Prefer:

1. Existing maintained project convention
2. Open standard or interoperable protocol
3. Maintained open-source library or framework
4. Provider-specific capability behind a narrow adapter
5. Small custom implementation with a recorded justification

## Build-versus-adopt gate

Before custom implementation, search the existing project and current ecosystem for:

- standard library support
- an existing project utility
- maintained open-source package
- official SDK
- stable protocol or file format
- reusable component from the project's design system

Record why candidates were accepted or rejected.

Do not build custom:

- authentication or authorization protocols
- cryptography
- routers
- form engines
- state-management frameworks
- UI component systems
- workflow engines
- parsers for established formats
- retry or queue infrastructure
- accessibility primitives

unless requirements genuinely exceed maintained options and the risk is understood.

## Portability contract

Separate:

- domain logic
- application orchestration
- storage and messaging interfaces
- provider adapters
- UI components and design tokens
- deployment configuration

Prefer:

- standard environment configuration
- documented interfaces
- portable data formats
- dependency injection or narrow adapter boundaries
- migrations that work outside one vendor runtime
- business logic that can run in ordinary tests
- explicit export and backup paths

Avoid:

- provider objects flowing through domain code
- hidden global configuration
- undocumented generated state
- proprietary behavior without a fallback
- vendor-specific syntax spread across the codebase
- coupling UI state directly to one backend implementation

## Dependency decision record

For every material new dependency, record:

```text
Need:
Existing project option:
Candidates checked:
Current evidence and date:
License:
Why selected:
Why not custom:
Portability boundary:
Removal or migration path:
Known risk:
Expected contribution to parent target:
Observed evidence and remaining validation gap:
```

The record is `DECISION READY` only when the named owner can select or reject the option with current compatibility, maintenance, license, portability, and migration risk resolved to the contracted threshold. Installation or a passing build alone is `ARTIFACT VERIFIED`.

## User-requested provider

When the user explicitly requests a provider or framework, use it unless unsafe or incompatible. Still keep domain logic portable and record the adapter boundary.

## Do not chase fashion

Do not migrate a working project merely because another framework is newer, trending, or preferred by the model.

A change must improve a material requirement such as:

- maintainability
- performance
- accessibility
- security
- ecosystem support
- deployment compatibility
- developer productivity
- user experience

and must justify migration cost.
