import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';

import { varAlpha } from 'src/theme/styles';
import { Iconify } from 'src/components/iconify';

// ----------------------------------------------------------------------

export type StatCardProps = {
  title: string;
  value: string;
  trend: number;
  icon: string;
  color?: 'primary' | 'secondary' | 'info' | 'success' | 'warning' | 'error';
};

export function StatCard({ title, value, trend, icon, color = 'primary' }: StatCardProps) {
  const trendIsPositive = trend >= 0;

  return (
    <Card>
      <Stack spacing={2} sx={{ p: 3 }}>
        <Stack direction="row" alignItems="center" justifyContent="space-between">
          <Box
            sx={{
              width: 48,
              height: 48,
              display: 'flex',
              borderRadius: 1.5,
              alignItems: 'center',
              justifyContent: 'center',
              color: `${color}.dark`,
              bgcolor: (theme) => varAlpha(theme.vars.palette[color].mainChannel, 0.16),
            }}
          >
            <Iconify icon={icon} width={24} />
          </Box>

          <Stack direction="row" alignItems="center" spacing={0.5}>
            <Iconify
              icon={trendIsPositive ? 'eva:trending-up-fill' : 'eva:trending-down-fill'}
              width={16}
              sx={{
                color: trendIsPositive ? 'success.main' : 'error.main',
              }}
            />
            <Typography
              variant="subtitle2"
              sx={{ color: trendIsPositive ? 'success.main' : 'error.main' }}
            >
              {trendIsPositive ? '+' : ''}
              {trend}%
            </Typography>
          </Stack>
        </Stack>

        <Stack spacing={0.5}>
          <Typography variant="h4">{value}</Typography>
          <Typography variant="body2" sx={{ color: 'text.secondary' }}>
            {title}
          </Typography>
        </Stack>

        <Typography variant="caption" sx={{ color: 'text.disabled' }}>
          {trendIsPositive ? 'Increased' : 'Decreased'} from last month
        </Typography>
      </Stack>
    </Card>
  );
}
