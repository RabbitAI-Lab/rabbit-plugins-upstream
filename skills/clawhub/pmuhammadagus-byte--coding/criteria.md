# Criteria for Code Conventions

Reference material for evaluating coding style choices. The agent consults this when the user asks it to apply a specific coding convention that the user has written.

## How to use
- The user specifies a convention, either in their own reference file or in a message.
- The agent applies that convention to the code output.
- If the convention is unclear, the agent asks the user for clarification before applying it.

## Examples of conventions
- Indentation: 2 or 4 spaces, consistent within a file.
- Naming: snake_case for files, camelCase for variables, or as the user specifies.
- Tests: colocated with source, or in a separate folder, as the user specifies.
- Comments: minimal, explain why not what.

The agent does not decide conventions on its own. It follows what the user explicitly provides and asks when something is ambiguous.
