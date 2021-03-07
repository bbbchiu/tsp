* file
* test.py:
    * 測試檔:
        * map_size: 地圖大小，目前地圖都方形，所以只取邊長
        * map_arr:  存地圖的array
* tsp.py:
    * tsp 演算法
    * 參數
        * self.initp        初始的點，出發點    
        * self.map_arr      存地圖的array    
        * self.map_size     存地圖的大小
        * self.map_struct   初始一張跟地圖一樣大小的圖
        * self.walk_arr     存near-neighbor方法的結果
        * self.travel_arr   存tsp方法的結果
        * self.min_arr      存最終最小的結果
        * self.min_cost     存最小的cost

    * function
        * init_map:  複製一張地圖
        * show_init: 展現初始資訊
        * get_cost:  算點到點的距離(cost)
        * walk:      call min_path function
        * show_result: 展現結果
        * visual_w:  視覺化 walk_arr 的結果
        * visual_t:  視覺化 travel_arr 的結果
        * visual_w:  視覺化 min_arr 的結果
        * min_path:  實作nearest-neighbor的方法
        * travel_path: 實作tsp的方法