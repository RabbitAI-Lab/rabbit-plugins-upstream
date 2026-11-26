"""A highlight-compressing HLG/BT.2020 to SDR/BT.709 transform."""
import numpy as np


def hlg_cube(path, strength):
    n = 41
    blue, green, red = np.mgrid[0:n, 0:n, 0:n] / (n-1)
    signal = np.stack([red, green, blue], axis=-1)
    a = .17883277
    b = 1-4*a
    c = .5-a*np.log(4*a)
    linear = np.where(signal <= .5, signal**2/3, (np.exp((signal-c)/a)+b)/12)
    y = linear @ [.2627, .6780, .0593]
    rec709 = linear @ np.array([[1.660491, -.587641, -.072850],
                                [-.124550, 1.132900, -.008349],
                                [-.018151, -.100579, 1.118730]]).T
    ratio = -np.expm1(-strength*y) / np.maximum(y, 1e-10)
    rgb = np.clip(rec709 * ratio[..., None], 0, 1)
    encoded = np.where(rgb < .018, 4.5*rgb, 1.099*rgb**.45-.099)
    with path.open('w') as output:
        output.write(f'LUT_3D_SIZE {n}\n')
        np.savetxt(output, encoded.reshape(-1, 3), fmt='%.6f')


def grade(video, directory, strength):
    transfer = video.get('color_transfer')
    if transfer == 'arib-std-b67':
        if video.get('color_primaries') != 'bt2020' or video.get('color_space') != 'bt2020nc':
            raise ValueError('Inspect this HLG source and select its actual input gamut/matrix.')
        hlg_cube(directory/'hlg.cube', 2.6 if strength is None else strength)
        return ('scale=in_color_matrix=bt2020:out_range=pc,format=gbrp16le,'
                'lut3d=hlg.cube,setparams=color_primaries=bt709:color_trc=bt709:colorspace=gbr:range=pc,'
                'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p')
    if transfer == 'smpte2084':
        raise ValueError('Use a PQ-specific HDR-to-SDR transform for this source.')
    if strength is not None:
        raise ValueError('--hlg-strength applies only to an HLG source.')
    return ('scale=out_color_matrix=bt709:out_primaries=bt709:out_transfer=bt709:out_range=tv,'
            'format=yuv420p')
