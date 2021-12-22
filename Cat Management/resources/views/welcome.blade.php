
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div class = "py-12">
    <div>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>breed</th>
            <th>color</th>
            <th>weight</th>
          </tr>
        </thead>
        <tbody>
          @foreach ($cats as $cat)
          <tr>{{ $cat->id}}</tr>
          <tr>{{ $cat->name}}</tr>
          <tr>{{ $cat->breed}}</tr>
          <tr>{{ $cat->color}}</tr>
          <tr>{{ $cat->weight}}</tr>

        </tbody>
        @endforeach
      </table>
    </div>
  </div>
  
</body>
</html>
