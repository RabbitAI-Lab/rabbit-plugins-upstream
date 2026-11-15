## Description:

Remove Watermark helps agents clean light-colored text watermarks from white-background document images using local image processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxttt](https://clawhub.ai/user/wxttt)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and document-processing agents use this skill to analyze document images, choose watermark regions and thresholds, run local cleanup commands, and verify that readable content remains intact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Watermark removal can unintentionally alter legitimate document content, especially when broad regions or full-image processing are used.

Mitigation: Keep original files, prefer tight region-based processing, review every output, and adjust only one parameter at a time when retrying.

Risk: Using the skill on official, evidentiary, or third-party documents may create legal or integrity concerns.

Mitigation: Use it only where document editing is permitted, and avoid applying it to official or evidentiary records.

Risk: The local script runs Python image-processing dependencies on user-provided files.

Mitigation: Run it in a pinned or isolated Python environment and process copies rather than originals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxttt/skills/remove-watermark)
- [Publisher profile](https://clawhub.ai/user/wxttt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance with inline bash commands and cleaned image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local processing; full-image mode requires scipy, while region mode uses Pillow and numpy.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
