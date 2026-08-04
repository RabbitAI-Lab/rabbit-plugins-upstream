## Description: <br>
Mubu Integration lets an agent manage Mubu outlines from the command line, including Markdown import/export, note lookup/export, and document or folder operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liuboacean](https://clawhub.ai/user/liuboacean) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to connect an agent to a Mubu account, import Markdown outlines into Mubu, export Mubu notes, search/list content, and manage documents or folders through CLI-backed workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use stored Mubu credentials to access and change real remote documents and folders. <br>
Mitigation: Install it only for agents that should access the Mubu account, keep MUBU credentials and ~/.mubu_token protected, and review targets and content before write actions. <br>
Risk: Some write commands can modify or move content without the confirmation behavior described in the documentation, while purge is permanent remote deletion. <br>
Mitigation: Manually confirm create, save, move, rename, delete, and purge operations; use --yes only after checking the target, and reserve purge for intentional permanent deletion. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liuboacean/skills/mubu-integration) <br>
- [Mubu API base endpoint](https://api2.mubu.com/v3/api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, XML, Shell commands, Configuration] <br>
**Output Format:** [Command-line text plus Markdown, JSON, OPML, or FreeMind XML exports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may read stored Mubu credentials and can create, save, move, rename, soft-delete, or permanently delete remote Mubu content when executed.] <br>

## Skill Version(s): <br>
1.3.10 (source: server release metadata, package __version__, and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
