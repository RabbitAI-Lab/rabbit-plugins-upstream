## Description: <br>
Helps agents create feed documents, upload feed content, submit Amazon SP-API Feeds, check processing status, retrieve feed documents, list feeds, and cancel feeds through LinkFox-provided scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and commerce operations agents use this skill to manage Amazon store feed submission workflows, including feed document creation, upload, submission, polling, cancellation, and result-document retrieval. It is intended for users who already have LinkFox API access and Amazon SP-API authorization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon feed data, feed document URLs, request bodies, and status responses may be saved locally. <br>
Mitigation: Run the skill only in workspaces approved for this data, review saved linkfox session files, and remove sensitive local outputs when they are no longer needed. <br>
Risk: The upload workflow sends a local file or inline content to a provided pre-signed upload URL. <br>
Mitigation: Verify the file path, content type, and destination URL before running upload_feed_document. <br>
Risk: The artifact contains conflicting cost guidance. <br>
Mitigation: Confirm LinkFox credit or cost behavior with the publisher before repeated feed operations. <br>


## Reference(s): <br>
- [Skill API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-feeds) <br>
- [Amazon createFeedDocument Reference](https://developer-docs.amazon.com/sp-api/reference/createfeeddocument) <br>
- [Amazon getFeedDocument Reference](https://developer-docs.amazon.com/sp-api/reference/getfeeddocument) <br>
- [Amazon createFeed Reference](https://developer-docs.amazon.com/sp-api/reference/createfeed) <br>
- [Amazon getFeed Reference](https://developer-docs.amazon.com/sp-api/reference/getfeed) <br>
- [Amazon getFeeds Reference](https://developer-docs.amazon.com/sp-api/reference/getfeeds) <br>
- [Amazon cancelFeed Reference](https://developer-docs.amazon.com/sp-api/reference/cancelfeed) <br>
- [Amazon Feed Type Values](https://developer-docs.amazon.com/sp-api/docs/feed-type-values) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, JSON, files, API calls] <br>
**Output Format:** [Markdown guidance with shell command examples; scripts emit JSON to stdout and save full JSON responses to local files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The scripts may summarize large responses on stdout while saving complete responses under a local linkfox session data directory.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
