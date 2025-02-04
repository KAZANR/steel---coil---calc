import math

# 定义钢的密度，单位：g/cm³
STEEL_DENSITY = 7.85

def calculate_steel_coil_info(weight, thickness, width, inner_diameter):
    """
    计算钢卷的长度和外径
    :param weight: 钢卷的重量，单位：kg
    :param thickness: 钢卷的厚度，单位：mm
    :param width: 钢卷的宽度，单位：mm
    :param inner_diameter: 钢卷的内径，单位：mm
    :return: 钢卷的长度（单位：m）和外径（单位：mm）
    """
    # 将重量从 kg 转换为 g
    weight_g = weight * 1000
    # 将厚度从 mm 转换为 cm
    thickness_cm = thickness / 10
    # 将宽度从 mm 转换为 cm
    width_cm = width / 10
    # 将内径从 mm 转换为 cm
    inner_diameter_cm = inner_diameter / 10

    # 计算钢卷的体积，单位：cm³
    volume = weight_g / STEEL_DENSITY

    # 计算钢卷圆环的横截面积，单位：cm²
    cross_section_area = volume / width_cm

    # 计算外径（单位：cm），根据圆环面积公式 S = π * ((D/2)² - (d/2)²)，推导出 D = sqrt(4*S/π + d²)
    outer_diameter_cm = math.sqrt(4 * cross_section_area / math.pi + inner_diameter_cm ** 2)
    # 将外径从 cm 转换为 mm
    outer_diameter_mm = outer_diameter_cm * 10

    # 计算钢卷的长度，单位：cm
    length_cm = volume / (thickness_cm * width_cm)
    # 将长度从 cm 转换为 m
    length_m = length_cm / 100

    return length_m, outer_diameter_mm

# 示例输入
weight = 10200  # kg
thickness = 1  # mm
width = 1000  # mm
inner_diameter = 610  # mm

# 调用函数计算钢卷的长度和外径
length, outer_diameter = calculate_steel_coil_info(weight, thickness, width, inner_diameter)

print(f"钢卷的长度为: {length:.2f} m")
print(f"钢卷的外径为: {outer_diameter:.2f} mm")
