## Description:

Builds and uses a user-calibrated Personal Context for a person through bounded interviews, explicit source consent, frozen task views, and user-reviewed context patches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bagel-ew](https://clawhub.ai/user/bagel-ew)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and agents use this skill to create, update, inspect, export, and apply purpose-limited personal context for downstream tasks such as job search, writing, speaking, collaboration, and decision preparation. It emphasizes user calibration, minimal disclosure, frozen Context Views, and pending Context Patches that require explicit review before long-term writeback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal Context Stores, Views, Patches, and exports may contain private or restricted personal information.

Mitigation: Use the documented authorization card before reading sources, keep default disclosure to public/current-task use, require explicit approval for private or restricted content, and review the exact Store, View, Patch, and export paths before creating files.

Risk: Context Views can be reused outside their intended audience, purpose, or validity window.

Mitigation: Validate each View before use, enforce exact subject, principal, audience, purpose, allowed_use, source_revision, and expires_at checks, and regenerate a new View when the Store or task changes.

Risk: Pending Patches, migrations, and purge operations can modify or remove local personal context if approved incorrectly.

Mitigation: Stage Patches without changing the canonical Store, apply only after reviewing the specific patch_id and proposals, run migration previews on copies where required, and use purge-plan plus plan_token approval before irreversible deletion.

Risk: Harness Memory or project history could be mistaken for confirmed Personal Context.

Mitigation: Treat Harness Memory and other history only as candidate evidence after explicit authorization; do not auto-import, auto-export, or mark those observations as confirmed without user calibration and patch review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bagel-ew/skills/brief-yourself)
- [Publisher Profile](https://clawhub.ai/user/bagel-ew)
- [Skill Entry](artifact/SKILL.md)
- [Personal Context Model](artifact/personal-context-model.md)
- [Source Consent And Disclosure](artifact/source-consent-and-disclosure.md)
- [Interview And Calibration](artifact/interview-and-calibration.md)
- [Context View And Patch Protocol](artifact/context-view-and-patch.md)
- [Harness Boundaries](artifact/harness-boundaries.md)
- [Store Operations](artifact/store-operations.md)
- [Context View Schema](artifact/context-view-v1.0.1.schema.json)
- [Context Patch Schema](artifact/context-patch-v1.0.1.schema.json)
- [Personal Context Store Schema](artifact/personal-context-store-v1.0.1.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Conversational guidance, Markdown briefs, JSON Store/View/Patch files, schema-compatible configuration, and shell command examples for local runtime operations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include user-facing briefs, candidate claims, tensions and unknowns, frozen Context Views, pending Context Patches, exports, validation results, and adapter-ready Markdown or JSON task context.]

## Skill Version(s):

1.0.1 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
