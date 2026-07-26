# Rule 3 — Components

Use MUI / Minimal UI components only. Never use native HTML form controls.

## Component map

| Purpose | Component |
|---------|-----------|
| Button | `Button` (variants: `text`, `outlined`, `contained`, `soft`) or `LoadingButton` |
| Select | `Select` + `MenuItem` |
| Autocomplete | `Autocomplete` |
| Text input | `TextField` |
| Checkbox | `Checkbox` + `FormControlLabel` |
| Radio | `Radio` + `FormControlLabel` |
| Switch | `Switch` |
| Date picker | `@mui/x-date-pickers` |
| Data table | `@mui/x-data-grid` |
| Dialog | `Dialog` |
| Tabs | `Tabs` / `Tab` or `CustomTabs` |
| Chip | `Chip` |
| Stepper | `Stepper` / `Step` / `StepLabel` |
| Alert | `Alert` |
| Card | `Card` / `CardContent` |
| Table | MUI `Table` family or `DataGrid` |
| Tooltip | `Tooltip` |
| Menu | `Menu` / `MenuItem` |
| Avatar | `Avatar` |
| Badge | `Badge` |
| Progress | `LinearProgress` / `CircularProgress` |
| Skeleton | `Skeleton` |
| Icons | `Iconify` from `src/components/iconify` |

## Buttons

Default theme props: `color="inherit"`, `disableElevation`.

- Primary CTA: `<Button variant="contained" color="primary">`
- Secondary: `<Button variant="outlined" color="inherit">` or `variant="soft"`
- Text action: `<Button variant="text">`
- Icon: `<IconButton>`
- Loading: `<LoadingButton>` from `@mui/lab`

## Forms

Wrap with `FormProvider` from `react-hook-form`. Use wrappers from `src/components/hook-form`:

- `RHFTextField`
- `RHFSelect`
- `RHFAutocomplete`
- `RHFCheckbox`
- `RHFSwitch`
- `RHFRadioGroup`
- `RHFDatePicker`
- `RHFUpload`

Validate with `zod` + `@hookform/resolvers`.

## Selects and autocomplete

Never render a native `<select>`. Always use `Select` with `MenuItem` or `Autocomplete`. In forms use `RHFSelect` / `RHFAutocomplete`.

## Date pickers

Use `@mui/x-date-pickers` inside `LocalizationProvider` with `AdapterDayjs`. Prefer `RHFDatePicker`.

## Tables

Use `DataGrid` for data tables. Define `GridColDef[]` columns with `field`, `headerName`, `flex`, `minWidth`, `renderCell`. Use MUI `Table` for simple read-only tables.
