## Description: <br>
搜好书 searches Anna's Archive for epub/pdf ebooks and augments results with book metadata, download links, and availability links across six Chinese book platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leisurelinux](https://clawhub.ai/user/leisurelinux) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to search for ebook metadata and discover source, download, and bookstore links for books requested by title, topic, author, or platform. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can surface third-party ebook download links, including content a user may not be authorized to access. <br>
Mitigation: Use it only for lawful access to content the user is authorized to obtain, and review returned links before use. <br>
Risk: Ordinary book requests may send search terms to Anna's Archive and several Chinese book platforms. <br>
Mitigation: Avoid sensitive queries and run network lookups only in approved environments. <br>
Risk: A WEREAD_API_KEY in the environment may be used automatically unless WeRead lookup is disabled. <br>
Mitigation: Omit the variable or invoke the script with --no-weread when WeRead lookup is not intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leisurelinux/skills/find-ebooks) <br>
- [Publisher profile](https://clawhub.ai/user/leisurelinux) <br>
- [Anna's Archive](https://annas-archive.gd) <br>
- [Douban Books](https://book.douban.com) <br>
- [iReader](https://www.ireader.com) <br>
- [Tmall Books](https://list.tmall.com) <br>
- [Dangdang](https://search.dangdang.com) <br>
- [JD Books](https://search.jd.com) <br>
- [CMP Book](https://www.cmpbook.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown-style tables and detail blocks, or JSON when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes complete single-line URLs; network results depend on third-party sources and optional proxy/API-key settings.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
