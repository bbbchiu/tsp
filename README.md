# tsp
* file
* test.py:
    * ������:
        * map_size: �a�Ϥj�p�A�ثe�a�ϳ���ΡA�ҥH�u�����
        * map_arr:  �s�a�Ϫ�array
* tsp.py:
    * tsp �t��k
    * �Ѽ�
        * self.initp        ��l���I�A�X�o�I    
        * self.map_arr      �s�a�Ϫ�array    
        * self.map_size     �s�a�Ϫ��j�p
        * self.map_struct   ��l�@�i��a�Ϥ@�ˤj�p����
        * self.walk_arr     �snear-neighbor��k�����G
        * self.travel_arr   �stsp��k�����G
        * self.min_arr      �s�̲׳̤p�����G
        * self.min_cost     �s�̤p��cost

    * function
        * init_map:  �ƻs�@�i�a��
        * show_init: �i�{��l��T
        * get_cost:  ���I���I���Z��(cost)
        * walk:      call min_path function
        * show_result: �i�{���G
        * visual_w:  ��ı�� walk_arr �����G
        * visual_t:  ��ı�� travel_arr �����G
        * visual_w:  ��ı�� min_arr �����G
        * min_path:  ��@nearest-neighbor����k
        * travel_path: ��@tsp����k