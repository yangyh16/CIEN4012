from shapely import wkt

def map_to_taxiZones(cbgs_nyc, taxi_zones):
    cbgs_nyc['taxi_object_id'] = None
    cbgs_nyc['taxi_geometry'] = None

    print(len(cbgs_nyc))
    for i in range(len(cbgs_nyc)):
        # print(i)
        if i%1000 == 0 :
            print(i)
        cbg_poly = cbgs_nyc.loc[i,'geometry']
        centroid_cbg = wkt.loads(cbgs_nyc.loc[i,'geometry'].centroid.wkt)
        for j in range(len(taxi_zones)):
            # print(i, j)
            taxi_poly = taxi_zones.loc[j,'geometry']
            if centroid_cbg.within(taxi_poly):
                taxi_obj_id = taxi_zones.loc[j,'objectid']
                cbgs_nyc['taxi_object_id'][i] = taxi_obj_id
                cbgs_nyc['taxi_geometry'][i] =  taxi_poly 
                break
    return cbgs_nyc