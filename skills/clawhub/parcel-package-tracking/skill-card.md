## Description: <br>
Track and add deliveries via Parcel API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gumadeiras](https://clawhub.ai/user/gumadeiras) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to list recent or active Parcel deliveries, add package tracking entries, and search supported carriers from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses PARCEL_API_KEY to call Parcel API endpoints, so an exposed key could allow package-tracking actions available to that key. <br>
Mitigation: Store PARCEL_API_KEY only in environment or secret storage, never paste it into chat or commit it, and rotate it if exposed. <br>
Risk: Installing a third-party skill gives its code access to actions permitted by the configured Parcel API key. <br>
Mitigation: Confirm the publisher handle gumadeiras is trusted before installation and scope or rotate credentials according to Parcel account practices. <br>


## Reference(s): <br>
- [Parcel web app](https://web.parcelapp.net) <br>
- [Parcel external API](https://api.parcel.app/external) <br>
- [Parcel supported carriers endpoint](https://api.parcel.app/external/supported_carriers.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text CLI output with Markdown usage examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PARCEL_API_KEY and network access to the Parcel API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
