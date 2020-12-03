import { Component,OnInit} from '@angular/core';
import {BhkserviceService} from './bhkservice.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'house-prediction';
  uiBHK:string;
  uiBathrooms:string;
  city_name=[]
  d={
    city:null,
    bhk:null,
    sqft:null,
    bath:null
  }
  price:String;

  constructor(private bhkprice:BhkserviceService){}
  ngOnInit() {

    this.bhkprice.getcities().subscribe((data:any[])=>{
      this.city_name=data["locations"];
      //console.log(this.city_name)
    })
    
  }

  onclick(sqft,city){
    this.d.city=city;
    this.d.bhk=this.uiBHK;
    this.d.bath=this.uiBathrooms;
    this.d.sqft=sqft;
    //console.log(this.d)
    this.bhkprice.getprice(this.d).subscribe((data:any[])=>{
      //console.log(data)
      this.price=String(data["price"])+"lac"
      console.log(this.price)
    })
  }

}
