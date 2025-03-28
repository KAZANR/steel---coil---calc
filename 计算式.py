import math
from typing import Tuple

# 常量命名全大写，添加单位注释
STEEL_DENSITY_G_PER_CM3 = 7.85  # 钢的密度 (g/cm³)
MM_TO_CM = 0.1                  # 毫米转厘米系数
KG_TO_G = 1000                  # 千克转克系数
CM_TO_M = 0.01                  # 厘米转米系数

def convert_units(value: float, conversion_factor: float) -> float:
    """通用单位转换函数"""
    return value * conversion_factor

def calculate_steel_coil_info(
    weight_kg: float,
    thickness_mm: float,
    width_mm: float,
    inner_diameter_mm: float
) -> Tuple[float, float]:
    """
    计算钢卷的长度和外径

    Args:
        weight_kg: 钢卷重量 (kg)
        thickness_mm: 钢材厚度 (mm)
        width_mm: 钢卷宽度 (mm)
        inner_diameter_mm: 钢卷内径 (mm)

    Returns:
        Tuple[长度(m), 外径(mm)]

    Raises:
        ValueError: 如果任何参数不是正数
    """
    # 参数验证
    if not all(x > 0 for x in (weight_kg, thickness_mm, width_mm, inner_diameter_mm)):
        raise ValueError("所有参数必须为正数")

    # 批量单位转换 (避免重复代码)
    weight_g = convert_units(weight_kg, KG_TO_G)
    thickness_cm = convert_units(thickness_mm, MM_TO_CM)
    width_cm = convert_units(width_mm, MM_TO_CM)
    inner_diameter_cm = convert_units(inner_diameter_mm, MM_TO_CM)

    # 计算体积 (cm³)
    volume_cm3 = weight_g / STEEL_DENSITY_G_PER_CM3

    # 计算长度 (优化公式，减少中间变量)
    length_m = convert_units(
        volume_cm3 / (thickness_cm * width_cm),
        CM_TO_M
    )

    # 计算外径 (使用命名变量提高可读性)
    cross_section_area_cm2 = volume_cm3 / width_cm
    outer_diameter_cm = math.sqrt(
        (4 * cross_section_area_cm2 / math.pi) + inner_diameter_cm**2
    )
    outer_diameter_mm = convert_units(outer_diameter_cm, 1/MM_TO_CM)

    return round(length_m, 2), round(outer_diameter_mm, 2)

# 示例用法
if __name__ == "__main__":
    try:
        length, diameter = calculate_steel_coil_info(
            weight_kg=10200,
            thickness_mm=1,
            width_mm=1000,
            inner_diameter_mm=610
        )
        print(f"钢卷长度: {length:,} m")      # 使用千位分隔符
        print(f"钢卷外径: {diameter:,.1f} mm") # 固定1位小数
    except ValueError as e:
        print(f"错误: {e}")
