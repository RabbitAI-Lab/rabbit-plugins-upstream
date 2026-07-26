## Description: <br>
Search and browse the MusicBrainz music encyclopedia, fetch Cover Art Archive images, resolve musicbrainz.org URLs, and submit user-approved tags, ratings, and collection edits when OAuth is configured. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to answer music metadata questions, retrieve discographies and cover art, resolve MusicBrainz identifiers or URLs, and manage the user's own MusicBrainz tags, ratings, or collections after explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OAuth-enabled write tools can change the user's own MusicBrainz tags, ratings, or collections after confirmation. <br>
Mitigation: Review the dry-run preview with the user and only repeat the tool call with confirm: true after explicit approval. <br>


## Reference(s): <br>
- [MusicBrainz](https://musicbrainz.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, API calls, guidance] <br>
**Output Format:** [Markdown or structured tool-call summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read workflows need no credentials; OAuth enables confirm-gated MusicBrainz account edits.] <br>

## Skill Version(s): <br>
0.2.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
