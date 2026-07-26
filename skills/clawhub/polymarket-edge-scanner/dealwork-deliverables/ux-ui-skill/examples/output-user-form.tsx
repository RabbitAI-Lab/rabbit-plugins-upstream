'use client';

import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { z } from 'zod';

import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import Stack from '@mui/material/Stack';
import MenuItem from '@mui/material/MenuItem';
import LoadingButton from '@mui/lab/LoadingButton';

import { Form, RHFTextField, RHFSelect, RHFSwitch } from 'src/components/hook-form';

// ----------------------------------------------------------------------

const ROLES = [
  { value: 'admin', label: 'Admin' },
  { value: 'editor', label: 'Editor' },
  { value: 'viewer', label: 'Viewer' },
];

const schema = z.object({
  fullName: z.string().min(2, 'Full name is required'),
  email: z.string().email('Enter a valid email'),
  role: z.string().min(1, 'Role is required'),
  isActive: z.boolean(),
  bio: z.string().optional(),
});

export type UserFormValues = z.infer<typeof schema>;

// ----------------------------------------------------------------------

type Props = {
  defaultValues?: Partial<UserFormValues>;
  onSubmit?: (data: UserFormValues) => void;
  isSubmitting?: boolean;
};

export function UserEditForm({ defaultValues, onSubmit, isSubmitting = false }: Props) {
  const methods = useForm<UserFormValues>({
    resolver: zodResolver(schema),
    defaultValues: {
      fullName: '',
      email: '',
      role: '',
      isActive: true,
      bio: '',
      ...defaultValues,
    },
  });

  const handleSubmit = methods.handleSubmit((data) => {
    onSubmit?.(data);
  });

  return (
    <Form methods={methods} onSubmit={handleSubmit}>
      <Card>
        <Stack spacing={3} sx={{ p: 3 }}>
          <Stack direction={{ xs: 'column', sm: 'row' }} spacing={2}>
            <RHFTextField name="fullName" label="Full name" />
            <RHFTextField name="email" label="Email" type="email" />
          </Stack>

          <Stack direction={{ xs: 'column', sm: 'row' }} spacing={2}>
            <RHFSelect name="role" label="Role">
              {ROLES.map((role) => (
                <MenuItem key={role.value} value={role.value}>
                  {role.label}
                </MenuItem>
              ))}
            </RHFSelect>

            <Box sx={{ display: 'flex', alignItems: 'center' }}>
              <RHFSwitch name="isActive" label="Active user" />
            </Box>
          </Stack>

          <RHFTextField name="bio" label="Bio" multiline rows={4} />

          <Stack direction="row" justifyContent="flex-end" spacing={1.5}>
            <LoadingButton
              type="submit"
              variant="contained"
              loading={isSubmitting}
              color="primary"
            >
              Save changes
            </LoadingButton>
          </Stack>
        </Stack>
      </Card>
    </Form>
  );
}
