#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    int R,C,F,N,B,T;
    //char x;
    ifstream inFile;

    inFile.open("example.in");
    if (!inFile) {
        cout << "Unable to open file";
        exit(1);
    }

    inFile >> R;
    inFile >> C;
    inFile >> F;
    inFile >> N;
    inFile >> B;
    inFile >> T;

    //cout << "Rows: " << R << endl;
    //cout << "Columns: " << C << endl;
    //cout << "Fleet: " << F << endl;
    //cout << "Rides: " << N << endl;
    //cout << "Bonus: " << B << endl;
    //cout << "Steps: " << T << endl;

    vector<vector<int>> cars;
    for(int i=0; i<F; i++){
      vector<int> car;
      car.push_back(i); //car no
      car.push_back(1); //availability: 0 or 1
      car.push_back(0); //x coordinate
      car.push_back(0); //y coordinate
      car.push_back(0); //time
      cars.push_back(car);
    }


    int a,b,x,y,s,t,distance;
    vector<vector<int>> vv;

    for(int i=0; i<N; i++){
      vector<int> v;
      inFile >> a;
      v.push_back(a);
      inFile >> b;
      v.push_back(b);
      inFile >> x;
      v.push_back(x);
      inFile >> y;
      v.push_back(y);
      inFile >> s;
      v.push_back(s);
      inFile >> t;
      v.push_back(t);
      //distance = (a-x)+(b-y);
      //v.push_back(distance);

      //cout << "from: [" << a << ","
      //      << b << "], to: [" << x << ","
      //      << y << "] earliest start: "
      //      << s << " latest finish: " << t << endl;
      vv.push_back(v);
    }

    inFile.close();
    return 0;
}
