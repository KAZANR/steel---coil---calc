import math

# 定义钢的密度，单位：g/cm³
STEEL_DENSITY = 7.85

def mm_to_cm(value):
    """
    将毫米转换为厘米
    :param value: 毫米值
    :return: 厘米值
    """
    return value / 10

def kg_to_g(value):
    """
    将千克转换为克
    :param value: 千克值
    :return: 克值
    """
    return value * 1000

def calculate_steel_coil_info(weight, thickness, width, inner_diameter):
    """
    计算钢卷的长度和外径
    :param weight: 钢卷的重量，单位：kg
    :param thickness: 钢卷的厚度，单位：mm
    :param width: 钢卷的宽度，单位：mm
    :param inner_diameter: 钢卷的内径，单位：mm
    :return: 钢卷的长度（单位：m）和外径（单位：mm）
    """
    # 输入参数校验
    if weight <= 0 or thickness <= 0 or width <= 0 or inner_diameter <= 0:
        raise ValueError("输入的参数必须为正数")
    
    # 单位转换
    weight_g = kg_to_g(weight)
    thickness_cm = mm_to_cm(thickness)
    width_cm = mm_to_cm(width)
    inner_diameter_cm = mm_to_cm(inner_diameter)

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

try:
    # 调用函数计算钢卷的长度和外径
    length, outer_diameter = calculate_steel_coil_info(weight, thickness, width, inner_diameter)
    print(f"钢卷的长度为: {length:.2f} m")
    print(f"钢卷的外径为: {outer_diameter:.2f} mm")
except ValueError as e:
    print(f"输入错误: {e}")
