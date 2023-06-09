import sys
import numpy as np
import time

def framework_search(*workshops):
    framework = []
    workshops = list(workshops)
    workshops_type9 = [workshop for workshop in workshops if workshop.type=='9']
    workshops_type8 = [workshop for workshop in workshops if workshop.type=='8']
    workshops_type7 = [workshop for workshop in workshops if workshop.type=='7']
    workshops_type6 = [workshop for workshop in workshops if workshop.type=='6']
    workshops_type5 = [workshop for workshop in workshops if workshop.type=='5']
    workshops_type4 = [workshop for workshop in workshops if workshop.type=='4']
    workshops_type3 = [workshop for workshop in workshops if workshop.type=='3']
    workshops_type2 = [workshop for workshop in workshops if workshop.type=='2']
    workshops_type1 = [workshop for workshop in workshops if workshop.type=='1']
    if len(workshops_type7) == 0: 
        workshop_7 = workshops_type9[0]
        point7 = np.array([float(workshop_7.locx), float(workshop_7.locy)])
        
        # tree1
        points_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type6))
        distance = np.sqrt(np.sum((points_6-point7)**2, axis=1))
        workshop_6 = workshops_type6[np.argmin(distance)]
        if len(workshops_type6) >= 2:
            workshops_type6.pop(np.argmin(distance))
        point6 = np.array([float(workshop_6.locx), float(workshop_6.locy)])
    
        points_3_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_6-point6)**2, axis=1))
        workshop_3_6 = workshops_type3[np.argmin(distance)]
        
        points_2_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_6-point6)**2, axis=1))
        workshop_2_6 = workshops_type2[np.argmin(distance)]

        framework1 = [
            (workshop_2_6, workshop_6),
            (workshop_3_6, workshop_6),
            (workshop_6, workshop_7),
        ]
        
        # tree2
        points_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type6))
        distance = np.sqrt(np.sum((points_6-point7)**2, axis=1))
        workshop_6 = workshops_type6[np.argmin(distance)]
        if len(workshops_type6) >= 2:
            workshops_type6.pop(np.argmin(distance))
        point6 = np.array([float(workshop_6.locx), float(workshop_6.locy)])
    
        points_3_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_6-point6)**2, axis=1))
        workshop_3_6 = workshops_type3[np.argmin(distance)]
        
        points_2_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_6-point6)**2, axis=1))
        workshop_2_6 = workshops_type2[np.argmin(distance)]

        framework2 = [
            (workshop_2_6, workshop_6),
            (workshop_3_6, workshop_6),
            (workshop_6, workshop_7),
        ]
        
        # tree3
        points_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type6))
        distance = np.sqrt(np.sum((points_6-point7)**2, axis=1))
        workshop_6 = workshops_type6[np.argmin(distance)]
        if len(workshops_type6) >= 2:
            workshops_type6.pop(np.argmin(distance))
        point6 = np.array([float(workshop_6.locx), float(workshop_6.locy)])
    
        points_3_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_6-point6)**2, axis=1))
        workshop_3_6 = workshops_type3[np.argmin(distance)]
        
        points_2_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_6-point6)**2, axis=1))
        workshop_2_6 = workshops_type2[np.argmin(distance)]

        framework3 = [
            (workshop_2_6, workshop_6),
            (workshop_3_6, workshop_6),
            (workshop_6, workshop_7),
        ]
        
        # tree4
        points_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type6))
        distance = np.sqrt(np.sum((points_6-point7)**2, axis=1))
        workshop_6 = workshops_type6[np.argmin(distance)]
        if len(workshops_type6) >= 2:
            workshops_type6.pop(np.argmin(distance))
        point6 = np.array([float(workshop_6.locx), float(workshop_6.locy)])
    
        points_3_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_6-point6)**2, axis=1))
        workshop_3_6 = workshops_type3[np.argmin(distance)]
        
        points_2_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_6-point6)**2, axis=1))
        workshop_2_6 = workshops_type2[np.argmin(distance)]

        framework4 = [
            (workshop_2_6, workshop_6),
            (workshop_3_6, workshop_6),
            (workshop_6, workshop_7),
        ]
        
        # tree5
        points_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type6))
        distance = np.sqrt(np.sum((points_6-point7)**2, axis=1))
        workshop_6 = workshops_type6[np.argmin(distance)]
        if len(workshops_type6) >= 2:
            workshops_type6.pop(np.argmin(distance))
        point6 = np.array([float(workshop_6.locx), float(workshop_6.locy)])
    
        points_3_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_6-point6)**2, axis=1))
        workshop_3_6 = workshops_type3[np.argmin(distance)]
        
        points_2_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_6-point6)**2, axis=1))
        workshop_2_6 = workshops_type2[np.argmin(distance)]

        framework5 = [
            (workshop_2_6, workshop_6),
            (workshop_3_6, workshop_6),
            (workshop_6, workshop_7),
        ]
        
        # tree6
        points_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type6))
        distance = np.sqrt(np.sum((points_6-point7)**2, axis=1))
        workshop_6 = workshops_type6[np.argmin(distance)]
        if len(workshops_type6) >= 2:
            workshops_type6.pop(np.argmin(distance))
        point6 = np.array([float(workshop_6.locx), float(workshop_6.locy)])
    
        points_3_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_6-point6)**2, axis=1))
        workshop_3_6 = workshops_type3[np.argmin(distance)]
        
        points_2_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_6-point6)**2, axis=1))
        workshop_2_6 = workshops_type2[np.argmin(distance)]

        framework6 = [
            (workshop_2_6, workshop_6),
            (workshop_3_6, workshop_6),
            (workshop_6, workshop_7),
        ]
        
        # tree7
        points_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type6))
        distance = np.sqrt(np.sum((points_6-point7)**2, axis=1))
        workshop_6 = workshops_type6[np.argmin(distance)]
        if len(workshops_type6) >= 2:
            workshops_type6.pop(np.argmin(distance))
        point6 = np.array([float(workshop_6.locx), float(workshop_6.locy)])
    
        points_3_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_6-point6)**2, axis=1))
        workshop_3_6 = workshops_type3[np.argmin(distance)]
        
        points_2_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_6-point6)**2, axis=1))
        workshop_2_6 = workshops_type2[np.argmin(distance)]

        framework7 = [
            (workshop_2_6, workshop_6),
            (workshop_3_6, workshop_6),
            (workshop_6, workshop_7),
        ]
        
        # tree8
        points_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type6))
        distance = np.sqrt(np.sum((points_6-point7)**2, axis=1))
        workshop_6 = workshops_type6[np.argmin(distance)]
        if len(workshops_type6) >= 2:
            workshops_type6.pop(np.argmin(distance))
        point6 = np.array([float(workshop_6.locx), float(workshop_6.locy)])
    
        points_3_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_6-point6)**2, axis=1))
        workshop_3_6 = workshops_type3[np.argmin(distance)]
        
        points_2_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_6-point6)**2, axis=1))
        workshop_2_6 = workshops_type2[np.argmin(distance)]

        framework8 = [
            (workshop_2_6, workshop_6),
            (workshop_3_6, workshop_6),
            (workshop_6, workshop_7),
        ]

        framework = framework1[:2] + framework2[:2] + framework3[:2] + framework4[:2] + framework5[:2] + framework6[:2] + framework7[:2] + framework8[:2] + [framework1[2], framework2[2], framework3[2], framework4[2], framework5[2], framework6[2], framework7[2], framework8[2]]
        
    elif len(workshops_type7) == 1: 
        workshop_8 = workshops_type8[0]
        point8 = np.array([float(workshop_8.locx), float(workshop_8.locy)])
        points_7 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type7))
        distance = np.sqrt(np.sum((points_7-point8)**2, axis=1))
        workshop_7 = workshops_type7[np.argmin(distance)]
        point7 = np.array([float(workshop_7.locx), float(workshop_7.locy)])
        
        # tree1
        points_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type6))
        distance = np.sqrt(np.sum((points_6-point7)**2, axis=1))
        workshop_6 = workshops_type6[np.argmin(distance)]
        if len(workshops_type6) >= 2:
            workshops_type6.pop(np.argmin(distance))
        point6 = np.array([float(workshop_6.locx), float(workshop_6.locy)])
        
        points_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type5))
        distance = np.sqrt(np.sum((points_5-point7)**2, axis=1))
        workshop_5 = workshops_type5[np.argmin(distance)]
        if len(workshops_type5) >= 2:
            workshops_type5.pop(np.argmin(distance))
        point5 = np.array([float(workshop_5.locx), float(workshop_5.locy)])
        
        points_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type4))
        distance = np.sqrt(np.sum((points_4-point7)**2, axis=1))
        workshop_4 = workshops_type4[np.argmin(distance)]
        if len(workshops_type4) >= 2:
            workshops_type4.pop(np.argmin(distance))
        point4 = np.array([float(workshop_4.locx), float(workshop_4.locy)])
        
        points_3_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_6-point6)**2, axis=1))
        workshop_3_6 = workshops_type3[np.argmin(distance)]
        
        points_2_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_6-point6)**2, axis=1))
        workshop_2_6 = workshops_type2[np.argmin(distance)]
        
        points_3_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_5-point5)**2, axis=1))
        workshop_3_5 = workshops_type3[np.argmin(distance)]
        
        points_1_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type1))
        distance = np.sqrt(np.sum((points_1_5-point5)**2, axis=1))
        workshop_1_5 = workshops_type1[np.argmin(distance)]

        points_2_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_4-point4)**2, axis=1))
        workshop_2_4 = workshops_type2[np.argmin(distance)]
        
        points_1_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type1))
        distance = np.sqrt(np.sum((points_1_4-point4)**2, axis=1))
        workshop_1_4 = workshops_type1[np.argmin(distance)]
        

        framework1 = [
            (workshop_1_4, workshop_4),
            (workshop_2_4, workshop_4),
            (workshop_1_5, workshop_5),
            (workshop_3_5, workshop_5),
            (workshop_2_6, workshop_6),
            (workshop_3_6, workshop_6),
            (workshop_4, workshop_7),
            (workshop_5, workshop_7),
            (workshop_6, workshop_7),
            (workshop_7, workshop_8),
        ]
        
        # tree2
        points_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type6))
        distance = np.sqrt(np.sum((points_6-point7)**2, axis=1))
        workshop_6 = workshops_type6[np.argmin(distance)]
        # workshops_type6.pop(np.argmin(distance))
        point6 = np.array([float(workshop_6.locx), float(workshop_6.locy)])
        
        points_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type5))
        distance = np.sqrt(np.sum((points_5-point7)**2, axis=1))
        workshop_5 = workshops_type5[np.argmin(distance)]
        # workshops_type5.pop(np.argmin(distance))
        point5 = np.array([float(workshop_5.locx), float(workshop_5.locy)])
        
        points_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type4))
        distance = np.sqrt(np.sum((points_4-point7)**2, axis=1))
        workshop_4 = workshops_type4[np.argmin(distance)]
        # workshops_type4.pop(np.argmin(distance))
        point4 = np.array([float(workshop_4.locx), float(workshop_4.locy)])
        
        points_3_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_6-point6)**2, axis=1))
        workshop_3_6 = workshops_type3[np.argmin(distance)]
        
        points_2_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_6-point6)**2, axis=1))
        workshop_2_6 = workshops_type2[np.argmin(distance)]
        
        points_3_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_5-point5)**2, axis=1))
        workshop_3_5 = workshops_type3[np.argmin(distance)]
        
        points_1_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type1))
        distance = np.sqrt(np.sum((points_1_5-point5)**2, axis=1))
        workshop_1_5 = workshops_type1[np.argmin(distance)]

        points_2_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_4-point4)**2, axis=1))
        workshop_2_4 = workshops_type2[np.argmin(distance)]
        
        points_1_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type1))
        distance = np.sqrt(np.sum((points_1_4-point4)**2, axis=1))
        workshop_1_4 = workshops_type1[np.argmin(distance)]
        
        framework2 = [
            (workshop_1_4, workshop_4),
            (workshop_2_4, workshop_4),
            (workshop_1_5, workshop_5),
            (workshop_3_5, workshop_5),
            (workshop_2_6, workshop_6),
            (workshop_3_6, workshop_6),
            (workshop_4, workshop_7),
            (workshop_5, workshop_7),
            (workshop_6, workshop_7),
            (workshop_7, workshop_8),
        ]
            
        framework = framework1[:6] + framework2[:6] + framework1[6:9] + framework2[6:9] + [(workshop_7, workshop_8), (workshop_7, workshop_8)]
            
    else:
        workshop_8 = workshops_type8[0]
        point8 = np.array([float(workshop_8.locx), float(workshop_8.locy)])
        
        # tree1
        points_7 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type7))
        distance = np.sqrt(np.sum((points_7-point8)**2, axis=1))
        workshop_7 = workshops_type7[np.argmin(distance)]
        if len(workshops_type7) >= 2:
            workshops_type7.pop(np.argmin(distance))
        point7 = np.array([float(workshop_7.locx), float(workshop_7.locy)])

        points_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type6))
        distance = np.sqrt(np.sum((points_6-point7)**2, axis=1))
        workshop_6 = workshops_type6[np.argmin(distance)]
        if len(workshops_type6) >= 2:
            workshops_type6.pop(np.argmin(distance))
        point6 = np.array([float(workshop_6.locx), float(workshop_6.locy)])
        
        points_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type5))
        distance = np.sqrt(np.sum((points_5-point7)**2, axis=1))
        workshop_5 = workshops_type5[np.argmin(distance)]
        if len(workshops_type5) >= 2:
            workshops_type5.pop(np.argmin(distance))
        point5 = np.array([float(workshop_5.locx), float(workshop_5.locy)])
        
        points_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type4))
        distance = np.sqrt(np.sum((points_4-point7)**2, axis=1))
        workshop_4 = workshops_type4[np.argmin(distance)]
        if len(workshops_type4) >= 2:
            workshops_type4.pop(np.argmin(distance))
        point4 = np.array([float(workshop_4.locx), float(workshop_4.locy)])
        
        points_3_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_6-point6)**2, axis=1))
        workshop_3_6 = workshops_type3[np.argmin(distance)]
        
        points_2_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_6-point6)**2, axis=1))
        workshop_2_6 = workshops_type2[np.argmin(distance)]
        
        points_3_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_5-point5)**2, axis=1))
        workshop_3_5 = workshops_type3[np.argmin(distance)]
        
        points_1_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type1))
        distance = np.sqrt(np.sum((points_1_5-point5)**2, axis=1))
        workshop_1_5 = workshops_type1[np.argmin(distance)]

        points_2_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_4-point4)**2, axis=1))
        workshop_2_4 = workshops_type2[np.argmin(distance)]
        
        points_1_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type1))
        distance = np.sqrt(np.sum((points_1_4-point4)**2, axis=1))
        workshop_1_4 = workshops_type1[np.argmin(distance)]
        
        framework1 = [
            (workshop_1_4, workshop_4),
            (workshop_2_4, workshop_4),
            (workshop_1_5, workshop_5),
            (workshop_3_5, workshop_5),
            (workshop_2_6, workshop_6),
            (workshop_3_6, workshop_6),
            (workshop_4, workshop_7),
            (workshop_5, workshop_7),
            (workshop_6, workshop_7),
            (workshop_7, workshop_8),
        ]
        
        # tree2
        points_7 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type7))
        distance = np.sqrt(np.sum((points_7-point8)**2, axis=1))
        workshop_7 = workshops_type7[np.argmin(distance)]
        if len(workshops_type7) >= 2:
            workshops_type7.pop(np.argmin(distance))
        point7 = np.array([float(workshop_7.locx), float(workshop_7.locy)])

        points_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type6))
        distance = np.sqrt(np.sum((points_6-point7)**2, axis=1))
        workshop_6 = workshops_type6[np.argmin(distance)]
        if len(workshops_type6) >= 2:
            workshops_type6.pop(np.argmin(distance))
        point6 = np.array([float(workshop_6.locx), float(workshop_6.locy)])
        
        points_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type5))
        distance = np.sqrt(np.sum((points_5-point7)**2, axis=1))
        workshop_5 = workshops_type5[np.argmin(distance)]
        if len(workshops_type5) >= 2:
            workshops_type5.pop(np.argmin(distance))
        point5 = np.array([float(workshop_5.locx), float(workshop_5.locy)])
        
        points_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type4))
        distance = np.sqrt(np.sum((points_4-point7)**2, axis=1))
        workshop_4 = workshops_type4[np.argmin(distance)]
        if len(workshops_type4) >= 2:
            workshops_type4.pop(np.argmin(distance))
        point4 = np.array([float(workshop_4.locx), float(workshop_4.locy)])
        
        points_3_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_6-point6)**2, axis=1))
        workshop_3_6 = workshops_type3[np.argmin(distance)]
        
        points_2_6 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_6-point6)**2, axis=1))
        workshop_2_6 = workshops_type2[np.argmin(distance)]
        
        points_3_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type3))
        distance = np.sqrt(np.sum((points_3_5-point5)**2, axis=1))
        workshop_3_5 = workshops_type3[np.argmin(distance)]
        
        points_1_5 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type1))
        distance = np.sqrt(np.sum((points_1_5-point5)**2, axis=1))
        workshop_1_5 = workshops_type1[np.argmin(distance)]

        points_2_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type2))
        distance = np.sqrt(np.sum((points_2_4-point4)**2, axis=1))
        workshop_2_4 = workshops_type2[np.argmin(distance)]
        
        points_1_4 = list(map(lambda x:[float(x.locx), float(x.locy)], workshops_type1))
        distance = np.sqrt(np.sum((points_1_4-point4)**2, axis=1))
        workshop_1_4 = workshops_type1[np.argmin(distance)]
        
        framework2 = [
            (workshop_1_4, workshop_4),
            (workshop_2_4, workshop_4),
            (workshop_1_5, workshop_5),
            (workshop_3_5, workshop_5),
            (workshop_2_6, workshop_6),
            (workshop_3_6, workshop_6),
            (workshop_4, workshop_7),
            (workshop_5, workshop_7),
            (workshop_6, workshop_7),
            (workshop_7, workshop_8),
        ]

        framework = framework1[:6] + framework2[:6] + framework1[6:9] + framework2[6:9] + [framework1[9], framework2[9]]

    return framework

    