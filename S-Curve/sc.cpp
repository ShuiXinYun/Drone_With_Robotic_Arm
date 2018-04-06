#include <cmath>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <fstream>

using namespace std;

const int SEGMENT_NUM = 7;

/* 7段式S曲线，用于舵机运动的平滑加减速控制，减少冲击 */
class S_Curev
{
    private:
    double S, T;
    double a, b;
    double ratio[SEGMENT_NUM];
    double t[SEGMENT_NUM], p[SEGMENT_NUM];
    double vp[SEGMENT_NUM], v_mat[SEGMENT_NUM][3];
    double sp[SEGMENT_NUM], s_mat[SEGMENT_NUM][4];
    
    private:
    void Time_Init(void)
    {
        for (int i = 0; i < SEGMENT_NUM; i++)
        t[i] = ratio[i] * T;
        
        p[0] = t[0];
        for (int i = 1; i < SEGMENT_NUM; i++)
        p[i] = p[i - 1] + t[i];
    }
    
    double calc_a(void)
    {
        double dividend = S * 6 * (t[4] + 2 * t[5] + t[6]);
        double divisor = -2 * p[5] * p[5] * t[0] + 4 * p[5] * p[6] * t[0] - 2 * p[6] * p[6] * t[0] - 4 * p[5] * p[5] * t[1] + 8 * p[5] * p[6] * t[1] - 4 * p[6] * p[6] * t[1] - 2 * p[5] * p[5] * t[2] +
        4 * p[5] * p[6] * t[2] - 2 * p[6] * p[6] * t[2] - p[3] * p[3] * (t[0] + 2 * t[1] + t[2]) + 2 * p[3] * p[4] * (t[0] + 2 * t[1] + t[2]) -
        p[4] * p[4] * (t[0] + 2 * t[1] + t[2]) + p[0] * p[0] * t[4] + 2 * p[1] * p[1] * t[4] - 4 * p[1] * p[2] * t[4] + 2 * p[2] * p[2] * t[4] + 3 * p[1] * t[1] * t[4] +
        3 * t[0] * t[2] * t[4] + 6 * t[1] * t[2] * t[4] + 3 * t[0] * t[3] * t[4] + 6 * t[1] * t[3] * t[4] + 3 * t[2] * t[3] * t[4] + 3 * t[0] * t[4] * t[4] + 6 * t[1] * t[4] * t[4] +
        3 * t[2] * t[4] * t[4] + 2 * p[0] * p[0] * t[5] + 4 * p[1] * p[1] * t[5] - 8 * p[1] * p[2] * t[5] + 4 * p[2] * p[2] * t[5] - 3 * p[5] * t[0] * t[5] + 6 * p[1] * t[1] * t[5] -
        6 * p[5] * t[1] * t[5] - 3 * p[5] * t[2] * t[5] + 6 * t[0] * t[2] * t[5] + 12 * t[1] * t[2] * t[5] + 3 * p[4] * (t[0] + 2 * t[1] + t[2])*t[5] +
        6 * t[0] * t[3] * t[5] + 12 * t[1] * t[3] * t[5] + 6 * t[2] * t[3] * t[5] + 6 * t[0] * t[4] * t[5] + 12 * t[1] * t[4] * t[5] + 6 * t[2] * t[4] * t[5] +
        6 * t[0] * t[5] * t[5] + 12 * t[1] * t[5] * t[5] + 6 * t[2] * t[5] * t[5] + p[0] * p[0] * t[6] + 2 * p[1] * p[1] * t[6] - 4 * p[1] * p[2] * t[6] + 2 * p[2] * p[2] * t[6] + 3 * p[1] * t[1] * t[6] +
        3 * t[0] * t[2] * t[6] + 6 * t[1] * t[2] * t[6] + 3 * t[0] * t[3] * t[6] + 6 * t[1] * t[3] * t[6] + 3 * t[2] * t[3] * t[6] + 3 * t[0] * t[4] * t[6] + 6 * t[1] * t[4] * t[6] +
        3 * t[2] * t[4] * t[6] + 3 * t[0] * t[5] * t[6] + 6 * t[1] * t[5] * t[6] + 3 * t[2] * t[5] * t[6] + 3 * t[0] * t[6] * t[6] + 6 * t[1] * t[6] * t[6] + 3 * t[2] * t[6] * t[6];//Thanks to mathematica...
        
        return dividend / divisor;
    }
    
    double calc_b(void)
    {
        return -a*(t[0] + 2 * t[1] + t[2]) / (t[4] + 2 * t[5] + t[6]);
    }
    
    void CalcBasicVars(void)
    {
        a = calc_a();
        b = calc_b();
    }
    
    void calc_vp(void)
    {
        vp[0] = a*0.5*t[0];
        vp[1] = vp[0] + a*t[1];
        vp[2] = vp[1] + a*0.5*t[2];
        vp[3] = vp[2];
        vp[4] = vp[3] + b*0.5*t[4];
        vp[5] = vp[4] + b*t[5];
        vp[6] = 0.0;
    }
    
    void calc_velocity_matrix(void)
    {
        v_mat[0][0] = 0; v_mat[0][1] = 0; v_mat[0][2] = 0.5*a / t[0];
        v_mat[1][0] = -0.5*a*p[0]; v_mat[1][1] = a; v_mat[1][2] = 0;
        v_mat[2][0] = vp[1] - a*p[1] / t[2] * (p[2] - 0.5*p[1]); v_mat[2][1] = a*p[2] / t[2]; v_mat[2][2] = -0.5*a / t[2];
        v_mat[3][0] = vp[2]; v_mat[3][1] = 0; v_mat[3][2] = 0;
        v_mat[4][0] = vp[3] + b*p[3] * p[3] / 2 / t[4]; v_mat[4][1] = -b*p[3] / t[4]; v_mat[4][2] = 0.5*b / t[4];
        v_mat[5][0] = vp[4] - b*p[4]; v_mat[5][1] = b; v_mat[5][2] = 0;
        v_mat[6][0] = vp[5] - b*(p[6] * p[5] - 0.5*p[5] * p[5]) / t[6]; v_mat[6][1] = b*p[6] / t[6]; v_mat[6][2] = -0.5*b / t[6];
    }
    
    void CalcVelocityVars(void)
    {
        calc_vp();
        calc_velocity_matrix();
    }
    
    void calc_sp(void)
    {
        sp[0] = a*pow(p[0], 2) / 6;
        for (int i = 1; i < SEGMENT_NUM; i++)
        {
            sp[i] = sp[i - 1];
            sp[i] += v_mat[i][0] * (p[i] - p[i - 1]);
            sp[i] += v_mat[i][1] * (pow(p[i], 2) - pow(p[i - 1], 2)) / 2;
            sp[i] += v_mat[i][2] * (pow(p[i], 3) - pow(p[i - 1], 3)) / 3;
        }
    }
    
    void calc_position_matrix(void)
    {
        s_mat[0][0] = 0; s_mat[0][1] = 0; s_mat[0][2] = 0; s_mat[0][3] = a / t[0] / 6;
        for (int i = 1; i < SEGMENT_NUM; i++)
        {
            s_mat[i][0] = sp[i - 1] - (v_mat[i][0] * p[i - 1] + v_mat[i][1] * pow(p[i - 1], 2) / 2 + v_mat[i][2] * pow(p[i - 1], 3) / 3);
            s_mat[i][1] = v_mat[i][0];
            s_mat[i][2] = v_mat[i][1] / 2;
            s_mat[i][3] = v_mat[i][2] / 3;
        }
    }
    
    void CalcPositionVars(void)
    {
        calc_sp();
        calc_position_matrix();
    }
    
    int calc_gap_index(double _t) const
    {
        int i = 0;
        while (i < SEGMENT_NUM && _t >= p[i])
        ++i;
        
        assert(i < SEGMENT_NUM);
        
        return i;
    }
    
    public:
    S_Curev(double totalLen, double totalTime, double _r0 = 0.05, double _r1 = 0.05, double _r2 = 0.05, double _r4 = 0.05, double _r5 = 0.05, double _r6 = 0.05) :S(totalLen), T(totalTime)
    {
        ratio[0] = _r0;
        ratio[1] = _r1;
        ratio[2] = _r2;
        ratio[3] = 1.0 - _r0 - _r1 - _r2 - _r4 - _r5 - _r6;
        ratio[4] = _r4;
        ratio[5] = _r5;
        ratio[6] = _r6;
        
        Time_Init();
        CalcBasicVars();
        CalcVelocityVars();
        CalcPositionVars();
    }
	
	double get_acc(double _t) const
	{
		if(_t<=p[0])
			return a/p[0]*_t;
		else if(_t<=p[1])
			return a;
		else if(_t<=p[2])
			return a*(1-(_t-p[1])/t[2]);
		else if(_t<=p[3])
			return 0;
		else if(_t<=p[4])
			return b*(_t-p[3])/t[4];
		else if(_t<=p[5])
			return b;
		else
			return b*(1-(_t-p[5])/t[6]);
	}
    
    double get_velocity(double _t) const
    {
        int i = calc_gap_index(_t);
        return v_mat[i][0] + _t*(v_mat[i][1] + _t*v_mat[i][2]);
    }
    
    double get_position(double _t) const
    {
        int i = calc_gap_index(_t);
        return s_mat[i][0] + _t*(s_mat[i][1] + _t*(s_mat[i][2] + _t *s_mat[i][3]));//Horner's rule
    }
};

int main(int argc, char **argv)
{
    ofstream fout("test.txt");
    
    double S = 100, T = 1000;
    auto curve = new S_Curev(S, T, 0.08, 0.14, 0.08, 0.08, 0.14, 0.08);
    double step = 0.01;
    
    double cur = 0;
    while (cur < T)
    {
        fout << cur << '\t' << curve->get_acc(cur) << '\t' << curve->get_velocity(cur) << '\t' << curve->get_position(cur) << endl;
        cur += step;
    }
    
    delete curve;
    fout.close();
    
    return 0;
}