## Description:

Artwork Lady embroidery-digitizing intake adapter that uses Playwright to log in to the Artwork Lady portal, fill the Embroidery Digitizing order form, attach one to three files, and either dry-run validation or submit the job when explicitly confirmed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, or operations agents use this skill to send embroidery digitizing jobs to Artwork Lady after another routine has selected the demand, downloaded attachments, and chosen field values. It is intended as a portal adapter that returns structured status so the calling workflow can update its own system only after a confirmed submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A confirmed run can submit a live Artwork Lady job and the portal does not provide a ticket id or built-in duplicate protection.

Mitigation: Run dry runs first, require explicit confirm:true for live submission, and have the calling workflow stamp job_reference plus submitted-at time and skip already-stamped demands.

Risk: Portal credentials, persisted Playwright sessions, screenshots, failure HTML, and uploaded customer artwork may contain sensitive data.

Mitigation: Protect environment variables, storage_state files, artifact directories, and uploaded files as sensitive data, and avoid pasting credentials into chat.

Risk: The skill automates a web portal whose form or login behavior may change.

Mitigation: Use the capture action to inspect the live field map after portal changes, and treat only an HTTP 200 response from order_form_submit as successful submission.

## Reference(s):

- [Artwork Lady skill page](https://clawhub.ai/zmtucker/skills/artworklady-digitizing)
- [Artwork Lady portal](https://www.artworklady.com)
- [Artwork Lady place-order form](https://www.artworklady.com/placeorder)
- [Placeorder flow notes](references/placeorder_flow_notes.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON command output with Markdown usage guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dry runs return filled-form status and diagnostics without submitting; confirmed submissions return structured submission status, response metadata, trace entries, and optional screenshot or failure artifacts.]

## Skill Version(s):

0.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
