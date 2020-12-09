import { getQueryPredicate } from '@angular/compiler/src/render3/view/util';
import { Injectable } from '@angular/core';
import { HttpClient,HttpErrorResponse} from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class BhkserviceService {
  url="http://127.0.0.1:5000/";

  constructor(private http: HttpClient) { 
  }
  getprice(value){
    
    console.log(value);
      return(this.http.post("http://127.0.0.1:5000/predict_price",value));
  }
  getcities(){
    return( this.http.get(this.url+"get_location_names"))

  }
}
