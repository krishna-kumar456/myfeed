export interface Todo {
  id: number;
  content: string;
}

export interface Card {
  id: string;
  by: string;
  title: string;
  summary: string;
  imageurl: string;
  url: string;
  descendants: string;
}
export interface Meta {
  totalCount: number;
}
