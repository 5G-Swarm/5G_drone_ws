# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from test/Fast.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import geometry_msgs.msg
import nav_msgs.msg
import sensor_msgs.msg
import std_msgs.msg

class Fast(genpy.Message):
  _md5sum = "7b1d4fd8deb79c38c49c3015662a7326"
  _type = "test/Fast"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """std_msgs/Header header
    uint32 seq
    time stamp
    string frame_id
uint8 uav_id
sensor_msgs/Image col
sensor_msgs/Image dep
nav_msgs/Odometry odom


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: nav_msgs/Odometry
# This represents an estimate of a position and velocity in free space.  
# The pose in this message should be specified in the coordinate frame given by header.frame_id.
# The twist in this message should be specified in the coordinate frame given by the child_frame_id
Header header
string child_frame_id
geometry_msgs/PoseWithCovariance pose
geometry_msgs/TwistWithCovariance twist

================================================================================
MSG: geometry_msgs/PoseWithCovariance
# This represents a pose in free space with uncertainty.

Pose pose

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/TwistWithCovariance
# This expresses velocity in free space with uncertainty.

Twist twist

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['header','seq','stamp','frame_id','uav_id','col','dep','odom']
  _slot_types = ['std_msgs/Header','uint32','time','string','uint8','sensor_msgs/Image','sensor_msgs/Image','nav_msgs/Odometry']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,seq,stamp,frame_id,uav_id,col,dep,odom

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Fast, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.seq is None:
        self.seq = 0
      if self.stamp is None:
        self.stamp = genpy.Time()
      if self.frame_id is None:
        self.frame_id = ''
      if self.uav_id is None:
        self.uav_id = 0
      if self.col is None:
        self.col = sensor_msgs.msg.Image()
      if self.dep is None:
        self.dep = sensor_msgs.msg.Image()
      if self.odom is None:
        self.odom = nav_msgs.msg.Odometry()
    else:
      self.header = std_msgs.msg.Header()
      self.seq = 0
      self.stamp = genpy.Time()
      self.frame_id = ''
      self.uav_id = 0
      self.col = sensor_msgs.msg.Image()
      self.dep = sensor_msgs.msg.Image()
      self.odom = nav_msgs.msg.Odometry()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.seq, _x.stamp.secs, _x.stamp.nsecs))
      _x = self.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B3I().pack(_x.uav_id, _x.col.header.seq, _x.col.header.stamp.secs, _x.col.header.stamp.nsecs))
      _x = self.col.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.col.height, _x.col.width))
      _x = self.col.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.col.is_bigendian, _x.col.step))
      _x = self.col.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.dep.header.seq, _x.dep.header.stamp.secs, _x.dep.header.stamp.nsecs))
      _x = self.dep.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.dep.height, _x.dep.width))
      _x = self.dep.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.dep.is_bigendian, _x.dep.step))
      _x = self.dep.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.odom.header.seq, _x.odom.header.stamp.secs, _x.odom.header.stamp.nsecs))
      _x = self.odom.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.odom.child_frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.odom.pose.pose.position.x, _x.odom.pose.pose.position.y, _x.odom.pose.pose.position.z, _x.odom.pose.pose.orientation.x, _x.odom.pose.pose.orientation.y, _x.odom.pose.pose.orientation.z, _x.odom.pose.pose.orientation.w))
      buff.write(_get_struct_36d().pack(*self.odom.pose.covariance))
      _x = self
      buff.write(_get_struct_6d().pack(_x.odom.twist.twist.linear.x, _x.odom.twist.twist.linear.y, _x.odom.twist.twist.linear.z, _x.odom.twist.twist.angular.x, _x.odom.twist.twist.angular.y, _x.odom.twist.twist.angular.z))
      buff.write(_get_struct_36d().pack(*self.odom.twist.covariance))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.stamp is None:
        self.stamp = genpy.Time()
      if self.col is None:
        self.col = sensor_msgs.msg.Image()
      if self.dep is None:
        self.dep = sensor_msgs.msg.Image()
      if self.odom is None:
        self.odom = nav_msgs.msg.Odometry()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.seq, _x.stamp.secs, _x.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.frame_id = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.uav_id, _x.col.header.seq, _x.col.header.stamp.secs, _x.col.header.stamp.nsecs,) = _get_struct_B3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.col.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.col.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.col.height, _x.col.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.col.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.col.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.col.is_bigendian, _x.col.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.col.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.dep.header.seq, _x.dep.header.stamp.secs, _x.dep.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.dep.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.dep.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.dep.height, _x.dep.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.dep.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.dep.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.dep.is_bigendian, _x.dep.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.dep.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.odom.header.seq, _x.odom.header.stamp.secs, _x.odom.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.odom.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.odom.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.odom.child_frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.odom.child_frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.odom.pose.pose.position.x, _x.odom.pose.pose.position.y, _x.odom.pose.pose.position.z, _x.odom.pose.pose.orientation.x, _x.odom.pose.pose.orientation.y, _x.odom.pose.pose.orientation.z, _x.odom.pose.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 288
      self.odom.pose.covariance = _get_struct_36d().unpack(str[start:end])
      _x = self
      start = end
      end += 48
      (_x.odom.twist.twist.linear.x, _x.odom.twist.twist.linear.y, _x.odom.twist.twist.linear.z, _x.odom.twist.twist.angular.x, _x.odom.twist.twist.angular.y, _x.odom.twist.twist.angular.z,) = _get_struct_6d().unpack(str[start:end])
      start = end
      end += 288
      self.odom.twist.covariance = _get_struct_36d().unpack(str[start:end])
      self.stamp.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.seq, _x.stamp.secs, _x.stamp.nsecs))
      _x = self.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B3I().pack(_x.uav_id, _x.col.header.seq, _x.col.header.stamp.secs, _x.col.header.stamp.nsecs))
      _x = self.col.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.col.height, _x.col.width))
      _x = self.col.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.col.is_bigendian, _x.col.step))
      _x = self.col.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.dep.header.seq, _x.dep.header.stamp.secs, _x.dep.header.stamp.nsecs))
      _x = self.dep.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.dep.height, _x.dep.width))
      _x = self.dep.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.dep.is_bigendian, _x.dep.step))
      _x = self.dep.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.odom.header.seq, _x.odom.header.stamp.secs, _x.odom.header.stamp.nsecs))
      _x = self.odom.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.odom.child_frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.odom.pose.pose.position.x, _x.odom.pose.pose.position.y, _x.odom.pose.pose.position.z, _x.odom.pose.pose.orientation.x, _x.odom.pose.pose.orientation.y, _x.odom.pose.pose.orientation.z, _x.odom.pose.pose.orientation.w))
      buff.write(self.odom.pose.covariance.tostring())
      _x = self
      buff.write(_get_struct_6d().pack(_x.odom.twist.twist.linear.x, _x.odom.twist.twist.linear.y, _x.odom.twist.twist.linear.z, _x.odom.twist.twist.angular.x, _x.odom.twist.twist.angular.y, _x.odom.twist.twist.angular.z))
      buff.write(self.odom.twist.covariance.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.stamp is None:
        self.stamp = genpy.Time()
      if self.col is None:
        self.col = sensor_msgs.msg.Image()
      if self.dep is None:
        self.dep = sensor_msgs.msg.Image()
      if self.odom is None:
        self.odom = nav_msgs.msg.Odometry()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.seq, _x.stamp.secs, _x.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.frame_id = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.uav_id, _x.col.header.seq, _x.col.header.stamp.secs, _x.col.header.stamp.nsecs,) = _get_struct_B3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.col.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.col.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.col.height, _x.col.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.col.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.col.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.col.is_bigendian, _x.col.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.col.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.dep.header.seq, _x.dep.header.stamp.secs, _x.dep.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.dep.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.dep.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.dep.height, _x.dep.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.dep.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.dep.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.dep.is_bigendian, _x.dep.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.dep.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.odom.header.seq, _x.odom.header.stamp.secs, _x.odom.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.odom.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.odom.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.odom.child_frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.odom.child_frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.odom.pose.pose.position.x, _x.odom.pose.pose.position.y, _x.odom.pose.pose.position.z, _x.odom.pose.pose.orientation.x, _x.odom.pose.pose.orientation.y, _x.odom.pose.pose.orientation.z, _x.odom.pose.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 288
      self.odom.pose.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
      _x = self
      start = end
      end += 48
      (_x.odom.twist.twist.linear.x, _x.odom.twist.twist.linear.y, _x.odom.twist.twist.linear.z, _x.odom.twist.twist.angular.x, _x.odom.twist.twist.angular.y, _x.odom.twist.twist.angular.z,) = _get_struct_6d().unpack(str[start:end])
      start = end
      end += 288
      self.odom.twist.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
      self.stamp.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_36d = None
def _get_struct_36d():
    global _struct_36d
    if _struct_36d is None:
        _struct_36d = struct.Struct("<36d")
    return _struct_36d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_6d = None
def _get_struct_6d():
    global _struct_6d
    if _struct_6d is None:
        _struct_6d = struct.Struct("<6d")
    return _struct_6d
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
_struct_B3I = None
def _get_struct_B3I():
    global _struct_B3I
    if _struct_B3I is None:
        _struct_B3I = struct.Struct("<B3I")
    return _struct_B3I
_struct_BI = None
def _get_struct_BI():
    global _struct_BI
    if _struct_BI is None:
        _struct_BI = struct.Struct("<BI")
    return _struct_BI
