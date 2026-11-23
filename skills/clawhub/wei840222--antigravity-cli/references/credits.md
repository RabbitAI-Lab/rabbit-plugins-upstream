# AI Credits

Source: <https://antigravity.google/docs/cli/credits/>. Quotas, consumption, and eligibility: <https://antigravity.google/docs/plans>.

The status line shows the balance, for example `AI Credits: 42`, and highlights it below the warning threshold. `/credits` opens usage, purchase, and subscription links. `/usage` (alias `/quota`) is model quota, not this panel.

`useG1Credits` in `~/.gemini/antigravity-cli/settings.json` spends personal credits after plan quota. Default `false`. Not available for business accounts. `/config` calls the same switch **Use G1 Credits**. Overages: <https://antigravity.google/docs/plans#overages>.

```json
{
  "useG1Credits": true
}
```

Leave it off unless the user asked to spend credits. On changes billing, not just the display.
