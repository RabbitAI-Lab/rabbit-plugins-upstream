# Get with Receipt for ClawHub

This directory is the complete ClawHub publication payload. It contains only a declarative skill
and supporting references. It does not include a custom OpenClaw plugin, executable hooks,
credentials, or a second commerce implementation.

The skill expects the native OpenClaw MCP connection named `receipt`. Installation and OAuth are
kept separate from the skill so ClawHub never handles Receipt credentials.
