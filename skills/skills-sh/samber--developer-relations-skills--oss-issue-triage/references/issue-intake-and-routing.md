# Issue intake and routing

Contents:

- what to ask on a form
- the template chooser as a routing layer
- tracker capabilities
- automation boundaries

## Ask only for what changes the outcome

A field earns its place when its absence forces a round-trip. Everything else trains reporters to skim the form.

**Bug report - the fields that decide the outcome**

| Field                                     | Required                      | Why                                                                                                                                                                              |
| ----------------------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| What happened / what you expected         | yes                           | The report's only irreducible content                                                                                                                                            |
| Minimal reproduction                      | yes                           | Node.js reduces its whole ask to this plus the description - a self-contained case using the project's own APIs, since a third-party wrapper hides whether the bug is even yours |
| Version                                   | yes, as a dropdown            | Free-text versions arrive as "latest"                                                                                                                                            |
| Environment (OS, runtime, install method) | yes                           | Decides reproducibility                                                                                                                                                          |
| Logs / output                             | yes, rendered as a code block | Screenshots of text are unsearchable                                                                                                                                             |
| Search-first confirmation                 | checkbox                      | Cuts duplicates measurably; costs the reporter one click                                                                                                                         |

**Feature request**

Order the fields:

1. Problem statement
2. Proposed solution
3. Alternatives

A form opening with "describe your solution" produces solutions to unstated problems, the hardest requests to triage.

**Usage question** - there should be no such form. Route it (below).

## The chooser is where routing happens

The list a reporter sees before typing is the highest-leverage surface in the system: it acts before any attention is spent.

- One entry per category the project wants, ordered deliberately (filename prefixes control order on most trackers: `01-bug`, `02-feature`).
- Off-tracker destinations for everything else: usage questions → forum, chat or discussions; security → the disclosure address; commercial or licensing → a contact address.
- Disable the blank/free-form option once the forms cover the real categories.
- Keep an explicit "something else" form if the project wants unclassifiable input - an undocumented dead end is worse than a wide door.

On GitHub this is `.github/ISSUE_TEMPLATE/config.yml` (`blank_issues_enabled`, `contact_links`); GitLab uses repository description templates. The mechanism differs, the design does not.

## Tracker capabilities to check before writing forms

- **Validated forms.** YAML issue forms (`.github/ISSUE_TEMPLATE/*.yml`) support text, textarea with code rendering, dropdown, multi-select, checkbox, file upload and markdown blocks, with `validations: required: true`. Markdown templates enforce nothing - the reporter can delete the whole body.
- **Auto-application.** A form can attach labels, an issue type, assignees and a title prefix on submission.
- **Org-wide defaults.** Default community health files ship one template set to every repository lacking its own - check before copying files by hand across repos.
- **Scripted fixes.** Some tracker CLIs cannot set every field (`gh issue create` cannot set an issue type; the REST API can). Check before scripting a bulk retrofit.

## The security path is not a routing entry

A contact link pointing at a security address is the visible part; the pipeline behind it is what matters, and every mature project runs the same three elements.

1. **A private intake channel** - a dedicated address, a bounty platform, or the code host's private vulnerability reporting; never the public tracker. With no security list, private vulnerability reporting is the default: it carries its own triage state and a private fork for collaborating on the fix.
2. **A named, size-capped response team**, distinct from general triage staff. Kubernetes caps its committee at ten members, nominated by sitting members, and acknowledges each report within three working days. Apache runs central triage across projects and lets mature projects request their own list once they can handle it.
3. **An embargo mechanism** for coordinated disclosure to downstream distributors before public release.

Two operational rules follow:

- A vulnerability reported publicly by mistake is an emergency: route it to the private channel immediately rather than triaging in the open.
- Staff it deliberately: security triage carries an isolation cost ordinary triage does not, because the work cannot be discussed with the wider project.

## Gating volume at the intake

When the valid share collapses, better forms do not help - the intake economics have to change. Options projects actually exercise, in rough order of reversibility:

- Require a reputation or contribution-history threshold before a submission is accepted.
- Cap the number of open submissions per author.
- Restrict issue or pull-request creation to collaborators, or turn a submission type off entirely - code hosts shipped these toggles in 2026 as a maintainer response to machine-generated contribution overload.
- Raise the submission cost: required reproduction, proof of concept, self-contained test case.
- Remove an incentive being farmed, including a monetary reward.

Gate on reputation and volume, not on whether content looks machine-generated. There is no reliable detector for the latter - OpenSSF's working group records that detection rests on maintainer intuition - and accusing a contributor without proof creates a conduct incident on top of the original problem.

## Automation boundaries

Automate classification and routing:

- path-based labelling fills the area axis from a PR's changed files
- owner files request review from the owning team, so the wait sits on a named group
- form-applied labels fill the type axis at submission
- the staleness sweep runs the waiting-on-reporter clock

Do not automate the first human sentence - the reasoning is in step 8.

## Retrofitting the existing queue

New intake only affects new items. For the existing backlog, either accept two vocabularies (old items keep their labels) or run a one-time bulk pass. Bulk-relabelling is scriptable through the tracker's API - do it in one batch, announce it, and expect notification volume to be the real cost.
