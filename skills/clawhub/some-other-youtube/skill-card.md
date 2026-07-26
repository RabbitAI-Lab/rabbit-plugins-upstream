## Description: <br>
Fetches YouTube video transcripts through the Apify API, supporting plain text and JSON output with optional language preference. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[inaor](https://clawhub.ai/user/inaor) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to retrieve YouTube transcripts from environments where direct YouTube transcript access may be blocked, then return the transcript as text or timestamped JSON. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: YouTube URLs are sent to Apify for third-party processing, which may have privacy, logging, and terms-of-use implications. <br>
Mitigation: Review YouTube and Apify terms before use, avoid submitting private or sensitive video URLs, and use the skill only when third-party processing is acceptable. <br>
Risk: The skill relies on proxy-backed transcript retrieval that may conflict with platform rules. <br>
Mitigation: Confirm that proxy-based retrieval is permitted for the intended workflow before deployment. <br>
Risk: The required Apify token grants access to an external paid service and may incur usage costs. <br>
Mitigation: Use a dedicated revocable Apify token, monitor Apify billing and quotas, and rotate the token if exposure is suspected. <br>


## Reference(s): <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [Apify Pricing](https://apify.com/pricing) <br>
- [Apify API Token](https://console.apify.com/account/integrations) <br>
- [YouTube Transcripts Actor](https://apify.com/karamelo/youtube-transcripts) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration] <br>
**Output Format:** [Plain text transcript or JSON with video metadata and timestamped transcript entries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write transcript output to a user-specified file and requires an APIFY_API_TOKEN environment variable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
