## Description:

Generate a 90-day HighLevel Social Planner CSV by using a client's sitemap for link-back URLs and post topics, then creating post copy and optional AI-generated images for each client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eddieflux](https://clawhub.ai/user/eddieflux)

### License/Terms of Use:

MIT-0

## Use Case:

Agencies, social media managers, and developers use this skill to generate client-specific social calendars for import into HighLevel Social Planner. It pulls client pages from a sitemap, writes scheduled posts around those URLs, and can generate and upload images for the CSV imageUrls column.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Client data and website-derived topics may be sent to selected AI and image providers.

Mitigation: Use only client data that is approved for those providers and confirm provider terms before generation.

Risk: Generated images can be uploaded to public web hosting and referenced in the CSV.

Mitigation: Verify the upload destination and public URL base before running, and review generated image files before importing the CSV.

Risk: FTP and broad SSH credentials can expose hosting accounts.

Mitigation: Prefer SSH with an explicitly supplied limited-purpose key, avoid FTP, and restrict the remote directory to the intended social media asset path.

Risk: Secrets passed on the command line may be retained in shell history or process listings.

Mitigation: Use approved secret handling for API keys and hosting credentials, and avoid placing long-lived secrets directly in reusable command examples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eddieflux/skills/social-90d-generator)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [Files, Text, Shell commands, Configuration]

**Output Format:** [CSV, JSON, PNG images, and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a HighLevel Social Planner import CSV, raw posts JSON, and optional local or uploaded image files; requires client details, a sitemap, AI provider credentials, and optional hosting credentials.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
