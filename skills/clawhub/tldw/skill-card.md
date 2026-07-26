## Description: <br>
Extracts YouTube video transcripts and provides concise summaries highlighting main points, arguments, and conclusions without watching the full video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vovavvk](https://clawhub.ai/user/vovavvk) <br>

### License/Terms of Use: <br>
AGPL-3.0 <br>


## Use Case: <br>
External users and developers use this skill to extract available YouTube captions or transcripts and turn them into concise summaries of a video's main points, arguments, and conclusions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser cookies can expose an authenticated YouTube session if stored, shared, or committed carelessly. <br>
Mitigation: Prefer public videos without cookies; when cookies are required, keep the cookie file outside shared or synced folders, never commit it, treat it like a password, and delete it after use. <br>
Risk: The transcript extractor weakens TLS certificate checks by default, which can reduce protection for authenticated or sensitive sessions. <br>
Mitigation: Review the extractor before installation and consider restoring certificate verification before using cookies or other authenticated access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vovavvk/skills/tldw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summary with optional JSON transcript extraction output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include video metadata such as title, duration, uploader, upload date, view count, and source URL when JSON extraction is used.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
