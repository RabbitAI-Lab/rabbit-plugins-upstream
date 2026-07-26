# Rule 5 — Forms

## Validation

Use `zod` schemas and `@hookform/resolvers`.

```tsx
import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { z } from 'zod';

const schema = z.object({
  email: z.string().email(),
  role: z.string().min(1),
});

type FormValues = z.infer<typeof schema>;

const methods = useForm<FormValues>({ resolver: zodResolver(schema) });
```

## Controlled wrappers

Use the project's `Form` component from `src/components/hook-form`. It wraps react-hook-form's `FormProvider` and renders a `<form>` element. Use the project's RHF wrappers from `src/components/hook-form` when they exist:

- `RHFTextField` for text inputs
- `RHFSelect` for selects
- `RHFAutocomplete` for autocomplete
- `RHFCheckbox` for checkboxes
- `RHFRadioGroup` for radio groups
- `RHFSwitch` for switches
- `RHFDatePicker` for dates
- `RHFUpload` for file uploads

The `starter-next-ts` variant only ships `RHFTextField`. If a wrapper does not exist in the target project, create a small controlled wrapper using `Controller` and MUI components, following the `RHFTextField` pattern.

```tsx
import { Form, RHFTextField, RHFSelect } from 'src/components/hook-form';

<Form methods={methods} onSubmit={onSubmit}>
  <RHFTextField name="email" label="Email" />
  <RHFSelect name="role" label="Role">
    <MenuItem value="admin">Admin</MenuItem>
    <MenuItem value="user">User</MenuItem>
  </RHFSelect>
</Form>
```

## Form layout

Use `Stack spacing={3}` for fields and `Stack direction="row"` for action buttons. Align submit buttons to the right with `justifyContent="flex-end"`.

## Error handling

RHF wrappers display `error?.message` as helper text. Keep helper text visible when no error: pass `helperText="Hint text"`.
