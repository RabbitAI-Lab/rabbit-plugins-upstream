---
name: wemol-cli-official
description: Use wemol-cli to search WeMol documentation, modules, and workflows for scientific knowledge and methods, and to run analyses and retrieve results. Use for concept questions, method explanations, comparisons, and workflow discovery in domains such as antibody and protein engineering, structural biology, and molecular modeling, even when the user does not mention WeMol or request computation. Also use for CLI setup, WeMol job submission, status, cancellation, and artifacts.
license: MIT-0
metadata: {"version":"1.2.1","cliVersion":"1.2.0","openclaw":{"homepage":"https://github.com/wecomput/wemol-cli","envVars":[{"name":"WEMOL_CLI_DATA_DIR","required":false,"description":"Optional existing WeMol CLI data directory; preserve it for every invocation."}]}}
---

# WeMol

Use standalone `wemol-cli` **1.2.0** to access WeMol. This is Skill version **1.2.1** of the organization-published ClawHub listing `@wecomput/wemol-cli`, using the Skill name `wemol-cli-official`. Its business guidance is adapted from the CLI's embedded Skill 0.3.0. The user signs in with `wemol-cli login` and manages accounts and approvals with `wemol-cli tui`; agents use the business commands directly.

The local runtime handles authentication, approvals, execution, and records. It starts automatically when needed. Install and update `@wecomput/wemol-cli` through ClawHub, then load it according to the agent host's rules. Users of the older `@nanomolar/wemol-cli` listing must explicitly switch to this organization listing; it is not an automatic update or ownership transfer. The bundled CLI installer installs a separate Skill named `wemol`; it does not update this ClawHub edition. If both editions are installed, choose which one the host should load to avoid duplicate or conflicting guidance; preserve personal edits.

## Local CLI

On first use or an installation request, follow [Setup](references/setup.md) to detect the execution environment and reuse or install CLI **1.2.0**. If it is missing and the user has requested WeMol setup/use, complete the verified installation as a prerequisite using the bundled [installer](scripts/install_cli.py), subject to the host's normal execution permissions. Installing the Skill folder itself does not execute a post-install hook: bootstrap runs when the agent next loads and uses this Skill. Do not install when the user restricts the task to advice or forbids software changes.

This Skill intentionally has no `requires.bins` gate, so its setup instructions remain available before the CLI is installed. The installer detects supported systems, checks pinned archive and executable SHA256 values, and never replaces an existing executable. Reuse a verified 1.2.0 installation; retain older/newer versions and resolve multiple installations using the setup guide. Use the returned absolute executable path consistently, including when it is not on PATH; do not repeat installation before every operation.

Preserve the user's `--data-dir` or `WEMOL_CLI_DATA_DIR` for every invocation, including login, status, and business commands. Examples below omit the optional data-directory argument. Run the CLI in the same environment and as the same system user that owns its configuration. Host-side installation does not make the CLI or credentials available inside a sandbox, container, WSL, or remote machine.

For installation, missing dependencies, migration, or login, read [Setup](references/setup.md). The bootstrap helper only installs a missing executable and probes `--version`; it does not start services, edit PATH or shell files, change data directories, or log in. Read-only `status` and `channels` checks follow installation using the existing data directory.

Requests contact the selected WeMol platform (default `https://wemol.wecomput.com`). Submission can upload scientific inputs and consume the account's quota or paid compute resources; downloads write result files locally. Public document access does not require login; account operations and computation require a WeMol account. Authentication stays in the local runtime; do not request passwords or API keys in chat or pass their values as command-line arguments.

## Core concepts

- A **channel** combines a service address and a login account. `wemol-cli channels` lists configured channels; use the returned `channel` name with `--channel`. Use a known name directly. To check identity, quota, or recent actions, use `channels --channel "channel-name"`. Ask the user when multiple choices are reasonable; do not switch accounts on your own.
- **Public documents** provide platform documentation and scientific or method explanations. Search them alongside modules and workflows, then read relevant document text for evidence. Document search and reading do not require login.
- A **capability** is a module or a workflow (Flow). Modules provide specific methods; workflows connect modules. Reuse the complete returned `capability`, such as `module:123` or `flow:456`, with `--capability`. Display names are for recognition and search; do not use them as operation references or construct IDs yourself.
- A **job** is an actual computation, identified by its channel and platform job ID. Names and tags can describe its purpose and help retrieve it later.
- **Artifacts** are files published by a job. Successful submission, completed computation, and complete file retrieval are separate facts.

The agent chooses evidence and suitable capabilities, supplies scientific inputs, interprets results, and decides whether job follow-up serves the task. The local runtime handles authentication, validation, approvals, uploads, submission, and downloads. When an operation requires login, give the user the `wemol-cli login` command with the same executable and data directory to run in their own terminal. For an existing channel, use `login --channel "channel-name"`.

## Knowledge retrieval and computation

For questions in the relevant scientific domains, use WeMol search to obtain documentation and method or workflow evidence before answering, unless sufficient relevant evidence is already available or the user restricts sources or tool use. A concept question is a reason to retrieve explanatory evidence; it does not need an execution request to activate this skill. Familiarity with a topic does not establish what the platform offers.

Search and reading are read-only. Finding a workflow can support an explanation of a practical path; preparing or submitting a computation requires the user's execution intent and suitable inputs. Keep the answer focused on the question and distinguish retrieved evidence from background knowledge and inference. Answer in the user's language.

## Read for the current purpose

- Plan or carry out a scientific task: check the [Task Guide index](guides/index.md), then read only a matching Guide. Guides define business methods and decision rules; use the operation references below to implement them with current capabilities. Reading a Guide does not establish execution intent.
- Explain a concept, understand a method, or discover capabilities, including synonym and Chinese/English query choices: [Knowledge and capability discovery](references/discover.md).
- Prepare parameters or submit computation: [Submit jobs](references/submit.md).
- Retrieve, observe, or cancel existing jobs: [Query jobs](references/jobs.md).
- Retrieve existing files: [Retrieve artifacts](references/deliver.md).

Read only the references needed for the task. Replace example values with actual values. Consult the command's `--help` when options are uncertain. Treat returned contracts, states, coverage, and errors as evidence.
