# ReUI components in this template

Generic interface controls in `references/template.html` are ReUI
components rather than hand-written markup. Reproduce this mapping when
generating a site from this template.

| Component | Instances | ReUI API |
| --- | --- | --- |
| Button | 25 | `<Button>` (with `asChild` for links) |
| Accordion | 6 | `<Accordion>` / `<AccordionItem>` / `<AccordionTrigger>` / `<AccordionContent>` |
| Form | 1 | `<Field>` / `<FieldLabel>` / `<FieldError>` + `<Input>` / `<Textarea>` / `<Select>` / `<RadioGroup>` / `<Checkbox>` / `<Button type="submit">` |
| Input | 1 | `<Input>` |
| Sheet | 1 | `<Sheet>` / `<SheetContent>` / `<SheetTitle>` |
| Toggle Group | 1 | `<ToggleGroup>` / `<ToggleGroupItem>` |

## How the markup declares them

`references/template.html` marks each control with `data-reui="<component>"`
and configures it with `data-reui-*` attributes; nested `data-reui-option`,
`data-reui-item`, `data-reui-field` and `data-reui-trigger` elements carry
the content. That indirection exists because the catalog demo has to be a
single self-contained file. **In a real project you do not reproduce the
attribute protocol — you import the ReUI components and pass props.**

```tsx
// what data-reui="select" means in a React/Next.js project
<Field>
  <FieldLabel htmlFor="project">Project type</FieldLabel>
  <Select value={value} onValueChange={setValue}>
    <SelectTrigger id="project"><SelectValue placeholder="Choose one" /></SelectTrigger>
    <SelectContent>
      <SelectItem value="identity">Identity</SelectItem>
    </SelectContent>
  </Select>
</Field>
```

## Styling contract

Components are shared; appearance is not. Two things carry this template's
identity, and neither forks a component:

1. ReUI's custom properties point at the template palette
   (`--primary`, `--background`, `--border`, `--radius`, font family).
2. Rendered controls keep the template's own class names, so its existing
   CSS — including contextual rules — still applies.

Keep icons on Lucide inline SVG. Emoji and dingbat glyphs are not icons.

## Verification

Check the rendered result, not the dependency list. For every control:
open it, choose with the keyboard, clear it, submit an empty required form,
confirm the error and `aria-invalid`, dismiss with Escape, and confirm focus
returns to the trigger. Check the mobile layout at 375px for horizontal
overflow and for tap targets under 44px.

Component source: ReUI (MIT), https://github.com/keenthemes/reui @ 8a2c701eaf95.
